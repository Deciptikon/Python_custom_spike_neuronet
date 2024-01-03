from abc import ABC, abstractmethod

class AbstractLayer(ABC):
    
    @abstractmethod
    def forward(self, input_data: list) -> list:
        pass
    
    ''' Этот метод под вопросом '''
    @abstractmethod
    def backward(self, gradient):
        pass
    

class AbstractSNN(ABC):
    
    @abstractmethod
    def train(self, input_data: list, target: list) -> None:
        pass
    
    @abstractmethod
    def predict(self, input_data: list) -> list:
        pass
    
    @abstractmethod
    def save_model(self, model_path: str) -> None:
        pass
    
    @abstractmethod
    def load_model(self, model_path: str) -> None:
        pass
    
    @abstractmethod
    def add_layer(self, layer: AbstractLayer) -> None:
        pass