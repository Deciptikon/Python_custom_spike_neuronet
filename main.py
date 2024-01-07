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
        '''Получаем состояние входного нейрона'''  
        state_neuron = False
        if self.input_obj != None:
            state_neuron = self.input_obj.get_state()
            
        '''Смещаем все спайки вправо по аксону, на 1'''    
        self.link.insert(0, state_neuron)
        self.link.pop()
        
        #print(len(self.T_links))
        '''Проверяем не пуст ли список тормозных аксонов'''
        if len(self.T_links) > 0:
            
            '''Для каждого набора присоединённых к этой ячейке
            тормозных аксонов'''
            for i in range(0, len(self.link) - 1):
                T_links = self.T_links[i]
                '''Проверяем не пуст ли список прикрепеленных тормозных аксонов'''
                if len(T_links) > 0:
                    '''проходим в каждый тормозной аксон'''
                    for T in T_links:
                        '''И если спайк в нем достиг точки крепления'''
                        if T.get_last_value():
                            '''тормозим сигнал в нормальном аксоне
                            в точке крепления'''
                            self.link[i] = False
                
    
    def print(self, prefix: str = '', type: str = 'None') -> None:
        if type in ['num' , 'number']:
            num_link = [1 if b else 0 for b in self.link]
            print(f'{prefix}{num_link}')
        else:
            print(f'{prefix}{self.link}')
        
    def set_input_obj(self, input_obj: 'Neuron' = None) -> None:
        self.input_obj = input_obj
    
    def set_length(self, length: int = 1) -> None:
        self.link = [False] * length
        
    def set_T_link(self, T_link: 'Link' = None, position: int | list[int] = 0) -> None:
        
        '''Локальная функция установки одной тормозной связи'''
        def set_one_T_link(self, T_link: 'Link' = None, position: int = 0) -> None:
            if position < len(self.link):
                if len(self.T_links) == 0:
                    self.T_links = [[]]*len(self.link)
                print(self.T_links)
                if len(self.T_links[position]) == 0:
                    self.T_links[position] = [T_link]
                    print(self.T_links)
                else:
                    self.T_links[position].append(T_link)
        
        if isinstance(position, int):
            set_one_T_link(self, T_link, position)
        elif isinstance(position, list) and all(isinstance(num, int) for num in position):
            for pos in position:
                set_one_T_link(self, T_link, pos)
            
    
    def get_last_value(self) -> bool:
        return self.link[len(self.link)-1]
        
    
class Neuron:
    def __init__(self) -> None:
        self.input_links: list[Link] = []
        self.state: bool = False
    
    def add_input_link(self, link: Link) -> None:
        self.input_links.append(link)
        
    def step(self) -> None:
        sig_arr = [link.get_last_value() for link in self.input_links]
        if True in sig_arr:
            self.state = True
        else:
            self.state = False
            
    def get_state(self) -> bool:
        return self.state
        
 
    

link = Link(length=7)
T_link = Link(length=7)
T_link2 = Link(length=7)


link.link[0] = True
link.link[1] = True
link.link[2] = True
link.link[3] = True
link.link[4] = True

T_link.link[5] = True
T_link2.link[5] = True

link.print(prefix='link    = ')
T_link.print(prefix='T-link  = ')
T_link2.print(prefix='T-link2 = ')



link.set_T_link(T_link=T_link, position=2)
link.set_T_link(T_link=T_link2, position=[2,5])


link.print(   prefix='link    = ', type='num')
T_link.print( prefix='T-link  = ', type='num')
T_link2.print(prefix='T-link2 = ', type='num')

k: int = 0
while True:
    print(f'   step {k}')
    
    link.step()
    T_link.step()
    T_link2.step()
    
    link.print(prefix='link    = ', type='num')
    T_link.print(prefix='T-link  = ', type='num')
    T_link2.print(prefix='T-link2 = ', type='num')
    
    time.sleep(1)
    k += 1
    if k > 10: break




    
    