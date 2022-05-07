# create a DNN using any platform you prefer  and test if it has better accuracy

# import the necessary packages
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import SGD
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True, help="path to the output loss/accuracy plot")
args = vars(ap.parse_args())

# grab the MNIST dataset (if this is the first time you are running this script, the download may take a minute)
print("[INFO] accessing MNIST...")
dataset = datasets.fetch_mldata("MNIST Original")

# plot the results
plt.plot(x, y, "b.")
plt.plot(x, y_predict, "r-")
plt.axis([-3, 3, 0, 10])
plt.show()

# use sklearn to fit a 9th degree polynomial model
from sklearn.preprocessing import PolynomialFeatures
poly_features = PolynomialFeatures(degree=9, include_bias=False)
x_poly = poly_features.fit_transform(x)
lin_reg = LinearRegression()
lin_reg.fit(x_poly, y)
y_predict = lin_reg.predict(x_poly)

# plot the results
plt.plot(x, y, "b.")
plt.plot(x, y_predict, "r-")
plt.axis([-3, 3, 0, 10])
plt.show()

# convert the model to pytorch
import torch
from torch.autograd import Variable

x_data = Variable(torch.Tensor([[1.0], [2.0], [3.0]]))
y_data = Variable(torch.Tensor([[2.0], [4.0], [6.0]]))

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, x):
        y_pred = self.linear(x)
        return y_pred

model = Model()

criterion = torch.nn.MSELoss(size_average=False)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(500):
    y_pred = model(x_data)

    loss = criterion(y_pred, y_data)
    print(epoch, loss.data[0])

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()


# create a bigger model with more layers
import torch
from torch.autograd import Variable

x_data = Variable(torch.Tensor([[1.0], [2.0], [3.0]]))
y_data = Variable(torch.Tensor([[2.0], [4.0], [6.0]]))

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear1 = torch.nn.Linear(1, 10)
        self.linear2 = torch.nn.Linear(10, 1)

    def forward(self, x):
        y_pred = self.linear2(self.linear1(x))
        return y_pred

model = Model()

criterion = torch.nn.MSELoss(size_average=False)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(500):
    y_pred = model(x_data)

    loss = criterion(y_pred, y_data)
    print(epoch, loss.data[0])

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

hour_var = Variable(torch.Tensor([[4.0]]))
y_pred = model(hour_var)
print("predict (after training)", 4, model(hour_var).data[0][0])
hour_var = Variable(torch.Tensor([[4.0]]))



class SelfAttention(torch.nn.Module):
    def __init__(self):
        super(SelfAttention, self).__init__()
        self.query_conv = nn.Conv2d(in_channels=512, out_channels=64, kernel_size=1)
        self.key_conv = nn.Conv2d(in_channels=512, out_channels=64, kernel_size=1)
        self.value_conv = nn.Conv2d(in_channels=512, out_channels=512, kernel_size=1)
        self.gamma = nn.Parameter(torch.zeros(1))

    def forward(self, x):
        B, C, H, W = x.size()
        proj_query = self.query_conv(x).view(B, -1, W*H).permute(0, 2, 1)
        proj_key = self.key_conv(x).view(B, -1, W*H)
        energy = torch.bmm(proj_query, proj_key)
        attention = F.softmax(energy, dim=-1)
        proj_value = self.value_conv(x).view(B, -1, W*H)

        out = torch.bmm(proj_value, attention.permute(0, 2, 1))
        out = out.view(B, C, H, W)

        out = self.gamma*out + x
        return out


class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear1 = torch.nn.Linear(1, 10)
        self.linear2 = torch.nn.Linear(10, 1)
        self.attention = SelfAttention()

    def forward(self, x):
        y_pred = self.linear2(self.linear1(x))
        return y_pred

model = Model()

criterion = torch.nn.MSELoss(size_average=False)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(500):
    y_pred = model(x_data)

    loss = criterion(y_pred, y_data)
    print(epoch, loss.data[0])

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

hour_var = Variable(torch.Tensor([[4.0]]))
y_pred = model(hour_var)
print("predict (after training)", 4, model(hour_var).data[0][0])
hour_var = Variable(torch.Tensor([[4.0]]))
