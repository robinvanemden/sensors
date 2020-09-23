# -*- coding: utf-8 -*-

"""
    JADS 2020 Data-Driven Food Value Chain course
    Introduction to Sensors

    Example minimal Pytorch RNN temperature model.
    Deep neural network to predict average greenhouse temperatures
    over the course of a day.

"""

from typing import Any
import logging
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

import data

# --- import data ---

sensor_df = data.read("data/one-month-every-5-minutes.csv")
data.printer(sensor_df)

# --- plot temperature sensor data ---

sensor_df["temp"] = sensor_df["Sensor kas 4 R (888) - Temperature (°C) - averages"]

sensor_df['hour'] = sensor_df.timestamp.dt.hour
sensor_df['day'] = sensor_df.timestamp.dt.day

# show plot for one temperature sensor
sensor_df.plot(x="timestamp", y=["temp"])
plt.show()

# --- Pytorch RNN temperature prediction ---

log = logging.getLogger(__name__)

BATCH_SIZE = 24
HIDDEN_SIZE = 256
NUM_LAYERS = 2
NUM_EPOCHS = 100
LEARNING_RATE = 0.005
DROPOUT = 0.2


class RNN(nn.Module):

    def __init__(self, input_size, hidden_size, output_size, n_layers=1, dropout=DROPOUT):

        super(RNN, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.n_layers = n_layers

        self.encoder = nn.Embedding(input_size, hidden_size)

        self.m = nn.Sequential(nn.ReLU(),
                               nn.Dropout(p=dropout),
                               nn.ReLU())

        self.decoder = nn.Linear(hidden_size, output_size)

    def forward(self, inp, hidden):

        inp = self.encoder(inp)
        output = self.m(inp)
        output = output.contiguous().view(-1, hidden.size(2))
        logits = self.decoder(output)

        return logits, hidden

    def init_hidden(self):
        return torch.zeros(self.n_layers, BATCH_SIZE, self.hidden_size).cpu()

    def _forward_unimplemented(self, *input_local: Any) -> None:
        pass


def main(local_temp_df):
    print_every = 10

    # short label column temperature
    local_temp_df["temp"] = local_temp_df["Sensor kas 4 R (888) - Temperature (°C) - averages"]

    # impute data for rows with missing values
    local_temp_df['temp'] = local_temp_df['temp'].fillna(method="ffill")

    # create timestamp based columns
    local_temp_df['hour'] = local_temp_df.timestamp.dt.hour
    local_temp_df['day'] = local_temp_df.timestamp.dt.day
    local_temp_df['minute'] = local_temp_df.timestamp.dt.minute

    # only use one of values per hour
    local_temp_df = local_temp_df.loc[local_temp_df.minute == 10]

    rnn = RNN(24, HIDDEN_SIZE, 1, n_layers=NUM_LAYERS)
    rnn.cpu()

    optimizer = torch.optim.Adam(rnn.parameters(), lr=LEARNING_RATE)
    criterion = torch.nn.MSELoss(reduction='mean')
    criterion.cpu()

    loss_avg = 0
    total_count = 0
    for epoch in range(0, NUM_EPOCHS + 1):

        # Shuffle
        df = local_temp_df.sample(frac=1)

        # Exclude day 31 in training - we will predict it later
        df = df.loc[local_temp_df.day != 31]

        # For every day in the sequence, create a batch of length 24 (each hour)
        for day in range(df.day.min(), df.day.max()):  #
            data = df.loc[df.day == day]

            inp = torch.LongTensor([int(i) for i in data.hour.values]).cpu()
            targets = torch.FloatTensor([float(f) for f in data.temp.values]).cpu()

            hidden = rnn.init_hidden()
            rnn.train()
            rnn.zero_grad()

            output, _ = rnn(inp, hidden)

            loss = criterion(output.reshape(-1), targets)

            loss_avg += loss.data.item()  # [ BATCHSIZE x SEQLEN ]

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_count += 1

        if epoch % print_every == 0:
            log.info("epoch=%d, %d%% loss=%.4f", epoch, epoch / NUM_EPOCHS * 100, loss_avg / total_count)

    # optional: save model
    # torch.save(rnn, "temperature-predictor")

    temps = []

    # Prediction stage: predict by hour
    for i in range(0, 24):
        rnn.eval()
        inp = torch.LongTensor([[i]]).cpu()

        hidden = rnn.init_hidden()
        logits, hidden = rnn(inp, hidden)
        pred = logits[-1, :].item()
        temps.append(pred)
        print("Average temp in month ", i, int(pred))

    # Compare against day 31, which was excluded from the training data
    day = local_temp_df.loc[local_temp_df.day == 31]

    plt.plot(day.hour, day.temp, label="predicted")
    plt.plot(day.hour, temps, label="actual (day 24)")
    plt.xlabel("time of day")
    plt.ylabel("temperature")

    L = plt.legend()
    L.get_texts()[0].set_text('observed')
    L.get_texts()[1].set_text('predicted')

    plt.show()


if __name__ == '__main__':
    main(sensor_df)
