import A3C_Fun as A3
from db import db_make
from multiprocessing import Manager
from CNS_UDP import *
from CNS_CFun import *


class body:
    def __init__(self):
        #==== Initial part for testing===========================================================#
        # self.a3c_mode : a3c모드의 여부와 에이전트의 갯수를 조정하는 곳이다.
        self.a3c_mode = {'mode': True, 'Nub_agent': 2, 'Range': range(0, 2)}
        self.shut_up = [True for _ in self.a3c_mode['Range']]
        #========================================================================================#
        self.shared_mem = [generate_mem().make_mem_structure() for _ in self.a3c_mode['Range']]
        #========================================================================================#
        self.UDP_net = [UDPSocket(self.shared_mem[_], IP='', Port=7001+_,
                                  shut_up=self.shut_up[_]) for _ in self.a3c_mode['Range']]

        if self.a3c_mode['mode']:
            clean_mem_list = [clean_mem(self.shared_mem[_], shut_up=self.shut_up[_]) for _ in self.a3c_mode['Range']]
            a3c_function_list = [A3.function1(self.shared_mem[_]) for _ in self.a3c_mode['Range']]
            self.process_list = clean_mem_list + a3c_function_list
        else:
            self.process_list = [
                clean_mem(self.shared_mem, shut_up=self.shut_up),
            ]

    def start(self):
        print('A3C test mode : {}'.format(self.a3c_mode['mode']))
        job_list = []
        for __ in self.UDP_net:
            __.start()
            job_list.append(__)
        time.sleep(1)
        for __ in self.process_list:
            __.start()
            job_list.append(__)
        for job in job_list:
            job.join()


class generate_mem:
    def make_test_mem(self):
        memory_dict = {'Test': 0, 'List_Test': []}
        return memory_dict

    def make_test_list_mem(self):
        memory_list = []
        return memory_list

    def make_CNS_time_mem(self):
        memory_list = []
        return memory_list

    def make_clean_mem(self):
        memory_dict = {'Clean': True}
        return memory_dict

    def make_main_mem_structure(self, max_len_deque=10, show_main_mem=False):

        memory_dict = db_make().make_db_structure(max_len_deque)

        # with open('./db.txt', 'r') as f:
        #     while True:
        #         temp_ = f.readline().split('\t')
        #         if temp_[0] == '':  # if empty space -> break
        #             break
        #         sig = 0 if temp_[1] == 'INTEGER' else 1
        #         memory_dict[temp_[0]] = {'V': 0, 'L': [], 'D': deque(maxlen=max_len_deque), "type": sig}
        #         # memory_dict[temp_[0]] = {'V': 0, 'L': [], 'D': deque(maxlen=max_len_deque), "type": sig,
        #         #                          'N_V': 0, 'N_L': [], 'N_D': deque(maxlen=max_len_deque)}  # Noise parameter

        ## DCSCommPid.ini 만드는 기능
        make_DCSCommPid = False
        if make_DCSCommPid:
            with open('./db.txt', 'r') as f:
                nub_line = -1
                while True:
                    temp_ = f.readline().split('\t')
                    if temp_[0] == '':
                        break
                    if nub_line != -1:  # 첫번째 헤더의 내용 제외하고 추가
                        with open('./DCSCommPid.ini', 'a') as f_pid:
                            if nub_line == 0:
                                f_pid.write('{}\t{}\t{}'.format(nub_line, temp_[0], temp_[1]))
                            else:
                                f_pid.write('\n{}\t{}\t{}'.format(nub_line, temp_[0], temp_[1]))
                    nub_line += 1

        if show_main_mem:
            print(memory_dict)
        return memory_dict

    def make_mem_structure(self, copy_mem_nub=1, show_mem_list=False):
        memory_list = [Manager().dict(self.make_main_mem_structure(max_len_deque=10)),  # [0]
                       Manager().dict(self.make_test_mem()),
                       Manager().list(self.make_test_list_mem()),
                       Manager().list(self.make_CNS_time_mem()),                        # [-2]
                       Manager().dict(self.make_clean_mem()),                           # [-1]
                       ]
        '''
        개인이 설계한 메모리를 추가로 집어 넣을 것.
        ex) 
            memory_list = [Manager().dict(self.make_main_mem_structure(max_len_deque=10)),
                           Manager().dict(자신이 설계한 메모리 구조)),
                           ...
                           Manager().dict(self.make_clean_mem()),]
        '''
        if show_mem_list:
            i = 0
            for __ in memory_list:
                print('{}번째 리스트|{}'.format(i, __))
                i += 1
        print('Mem_List 생성 완료')
        return memory_list
# ====================================================================================================================#
import tensorflow as tf
from keras import backend as K
from keras.layers import Dense, Input, Conv1D, MaxPooling1D, LSTM, Flatten
from keras.models import Model
from keras.optimizers import Adam, RMSprop
from keras import backend as K


class A3C_main_network:
    def __init__(self):
        pass

    def build_network_model(self, net_type='DNN', in_pa=1, ou_pa=1, time_leg=1):
        # 네트워크 모델 - 의존성 없음
        if True:
            if net_type == 'DNN':
                state = Input(batch_shape=(None, in_pa))
                shared = Dense(32, input_dim=in_pa, activation='relu', kernel_initializer='glorot_uniform')(state)
                # shared = Dense(48, activation='relu', kernel_initializer='glorot_uniform')(shared)

            elif net_type == 'CNN' or net_type == 'LSTM' or net_type == 'CLSTM':
                state = Input(batch_shape=(None, time_leg, in_pa))
                if net_type == 'CNN':
                    shared = Conv1D(filters=10, kernel_size=3, strides=1, padding='same')(state)
                    shared = MaxPooling1D(pool_size=2)(shared)
                    shared = Flatten()(shared)

                elif net_type == 'LSTM':
                    shared = LSTM(16, activation='relu')(state)

                elif net_type == 'CLSTM':
                    shared = Conv1D(filters=10, kernel_size=3, strides=1, padding='same')(state)
                    shared = MaxPooling1D(pool_size=2)(shared)
                    shared = LSTM(8)(shared)

            # ----------------------------------------------------------------------------------------------------
            # Common output network
            actor_hidden = Dense(8, activation='relu', kernel_initializer='glorot_uniform')(shared)
            action_prob = Dense(ou_pa, activation='softmax', kernel_initializer='glorot_uniform')(actor_hidden)

            value_hidden = Dense(4, activation='relu', kernel_initializer='he_uniform')(shared)
            state_value = Dense(1, activation='linear', kernel_initializer='he_uniform')(value_hidden)

            actor, critic = Model(inputs=state, outputs=action_prob), Model(inputs=state, outputs=state_value)
            print('Make {} Network'.format(net_type))

            actor._make_predict_function()
            critic._make_predict_function()

        # actor.summary(print_fn=logging.info)
        # critic.summary(print_fn=logging.info)

        return actor, critic


if __name__ == '__main__':
    main_process = body()
    main_process.start()