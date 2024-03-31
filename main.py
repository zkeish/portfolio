import torch
import torch.nn as nn
import torch.optim as optim

# Define the neural network model
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.fc = nn.Linear(1, 1).to(device)  # Input size: 1, Output size: 1

    def forward(self, x):
        return self.fc(x)

# Function to train the model
def train_model(model, input_data, target_data, num_epochs=5000, learning_rate=0.01):
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=learning_rate)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    for epoch in range(num_epochs):
        inputs = torch.tensor(input_data, dtype=torch.float32).unsqueeze(1).to(device)  # Add dimension for batch
        targets = torch.tensor(target_data, dtype=torch.float32).unsqueeze(1).to(device)  # Add dimension for batch

        # Forward pass
        outputs = model(inputs)
        loss = criterion(outputs, targets)

        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (epoch+1) % 10 == 0:
            print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))

# Function to make predictions
def predict(model, input_value):
    with torch.no_grad():
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        input_tensor = torch.tensor([[input_value]], dtype=torch.float32).to(device)  # Add dimension for batch
        output_tensor = model(input_tensor)
        return output_tensor.item()

# Example usage
if __name__ == "__main__":
    # Suppose we want to train the model to output the square of the input value
    # input_data = [1, 2, 3, 4, 5]  # Single input values
    # target_data = [1, 4, 9, 16, 25]  # Output data: square of each input value

    def square_list(length):
        input_list = list(range(1, length + 1))
        squared_list = [x**2 for x in input_list]
        return input_list, squared_list
    
    input_data, target_data = square_list(6)
    model = SimpleNN()
    train_model(model, input_data, target_data)

    # Test the trained model
    test_input = 6
    predicted_output = predict(model, test_input)
    print("Predicted output for input {}: {}".format(test_input, predicted_output))
