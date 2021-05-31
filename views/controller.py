from kaggletitanic.models.dataset import Dataset
from kaggletitanic.models.service import Service


class Controller(object):
    dataset = Dataset()
    service = Service()

    def modeling(self, train, test) -> object:
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this

    def preprocess(self, train, test) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        print(f'Train의 type 은 {type(this)} 이다')
        print(f'Train의 column 은 {this.train.columns} 이다')
        print(f'Test의 type 은 {type(this.test)} 이다')
        print(f'Test의 column 은 {this.test.columns} 이다')
        return this
