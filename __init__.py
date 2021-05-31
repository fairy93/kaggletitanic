from titanic.views.controller import Controller

if __name__ == '__main__':
    controller = Controller()
    while True:
        m = int(input('0 break 1 모델링'))
        if m == 0:
            break
        elif m == 1:
            controller.preprocess('train.csv')
        else:
            break
