from abc import ABC, abstractmethod
import time

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


class Link:
    def __init__(self, length: int = 1, input_obj: 'Neuron' = None) -> None:
        self.link: list[bool] = [False] * length
        self.input_obj: Neuron = input_obj
        self.T_links: list[list[Link]] = []
    
    def step(self) -> None:
        self.link = [False] + self.link[:-1]
        
    def step2(self) -> None:
        self.link.insert(0, False)
        self.link.pop()
    
    def print(self, prefix: str = ''):
        print(f'{prefix}{self.link}')
        
    def set_input_obj(self, input_obj: 'Neuron' = None) -> None:
        self.input_obj = input_obj
    
    def set_length(self, length: int = 1) -> None:
        self.link = [False] * length
        
    def set_T_link(self, link: 'Link' = None, position: int = 0):
        if position < len(self.link):
            pass
    
class Neuron:
    def __init__(self) -> None:
        input_links: list[Link] = []
        output_links: list[Link] = []
    
    def app_input_link(self, link: Link) -> None:
        self.input_links.append(link)
 
    

link = Link(length=7)
T_link = Link(length=7)

link.link.insert(2, True)
T_link.link.insert(2, True)

link.print(prefix='link   = ')
T_link.print(prefix='T-link = ')


link.step()
T_link.step()

link.print(prefix='link   = ')
T_link.print(prefix='T-link = ')
    
    