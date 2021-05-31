from kaggletitanic.views.controller import Controller
from kaggletitanic.views.test import Test
from kaggletitanic.templates.plot import Plot

if __name__ == '__main__':
    while 1:
        menu = '2'
        # menu = input('0-exit 1-data visualization\n'
        #              ' 2-modeling\n'
        #              ' 3-machine learning\n'
        #              ' 4-machine release ')

        if menu == '0':
            break
        elif menu == '1':
            plot = Plot('train.csv')
            # plot.draw_survived_dead()
            # plot.draw_pclass()
            # plot.draw_sex()
            plot.draw_embarked()
        elif menu == '2':  # 컨트롤 클릭하면넘어가져
            controller = Controller()
            controller.modeling('train.csv', 'test.csv')
            break
        elif menu == '3':
            pass
        elif menu == '4':
            pass
        else:
            continue
