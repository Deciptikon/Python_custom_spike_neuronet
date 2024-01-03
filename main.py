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
        '''Смещаем все спайки вправо по аксону, на 1'''
        self.link.insert(0, False)
        self.link.pop()
        
        print(len(self.T_links))
        '''Проверяем не пуст ли список тормозных аксонов'''
        if len(self.T_links) > 0:
            
            '''Для каждого набора присоединённых к этой ячейке
            тормозных аксонов'''
            for i in range(0, len(self.link) - 1):
                T_links = self.T_links[i]
                '''Проверяем не пуст ли список прикрепеленных тормозных аксонов'''
                if len(T_links) > 0:
                    '''проходим в каждый аксон'''
                    for T in T_links:
                        '''И если спайк в нем достиг точки крепления'''
                        if T.get_last_value():
                            '''тормозим сигнал в нормальном аксоне
                            в точке крепления'''
                            self.link[i] = False
                
            
        
    
    def print(self, prefix: str = ''):
        print(f'{prefix}{self.link}')
        
    def set_input_obj(self, input_obj: 'Neuron' = None) -> None:
        self.input_obj = input_obj
    
    def set_length(self, length: int = 1) -> None:
        self.link = [False] * length
        
    def set_T_link(self, T_link: 'Link' = None, position: int = 0):
        if position < len(self.link):
            if len(self.T_links) == 0:
                self.T_links = [[]]*len(self.link)
            print(self.T_links)
            if len(self.T_links[position]) == 0:
                self.T_links[position] = [T_link]
                print(self.T_links)
            else:
                self.T_links[position].append(T_link)
    
    def get_last_value(self) -> bool:
        return self.link[len(self.link)-1]
        
    
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

link.set_T_link(T_link=T_link, position=2)
link.set_T_link(T_link=T_link, position=5)

link.step()
T_link.step()

link.print(prefix='link   = ')
T_link.print(prefix='T-link = ')
    
    