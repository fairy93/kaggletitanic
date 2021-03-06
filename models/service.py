from kaggletitanic.models.dataset import Dataset
import pandas as pd
import numpy as np


class Service(object):
    dataset = Dataset()

    def new_model(self, payload):
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1)

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, *feature) -> object:
        for i in feature:
            this.train = this.train.drop([i], axis=1)
            this.test = this.test.drop([i], axis=1)
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        # this.train = this.train.fillna({'Embarked': 'S'})
        # this.test = this.test.fillna({'Embarked': 'S'})
        # print(f'타입체크 {type(this.train["Embarked"])}')
        # this.train['Embarked'] = this.train['Embarked'].map({'S': '1', 'S': '2', 'S': '3'})

        this.train = this.train.fillna({'Embarked': 'S'})
        this.test = this.test.fillna({'Embarked': 'S'})
        this.train['Embarked'] = this.train['Embarked'].map({'S': 1, 'C': 2, 'Q': 3})
        this.test['Embarked'] = this.test['Embarked'].map({'S': 1, 'C': 2, 'Q': 3})
        return this

    @staticmethod
    def title_norminal(this) -> object:
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
        for dataset in combine:
            dataset['Title'] = dataset['Title'].replace(
                ['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona'])
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Mlle', 'Mr')
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] = dataset['Title'].replace('Mme', 'Rare')
            title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
            this.train['Title'] = this.train['Title'].fillna(0)
            this.test['Title'] = this.test['Title'].map(
                {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6})

            return this

    # @staticmethod
    # def gender_norminal(this):
    #     combine = [this.train, this.test]
    #     gender_mapping = {'male': 0, 'famale': 1}
    #     for i in combine:
    #         i['Gender'] = i['Sex'].map(gender_mapping)
    #
    #     this.train = combine[0]
    #     this.test = combine[1]
    #     return this
    @staticmethod
    def gender_norminal(this) -> object:
        combine = [this.train, this.test]
        gender_mapping = {'male': 0, 'female': 1}
        for i in combine:
            i['Gender'] = i['Sex'].map(gender_mapping)
        return this

    @staticmethod
    def age_ordinal(this) -> object:
        train = this.train
        test = this.test
        train['Age'] = train['Age'].fillna(-0, 5)
        train['Age'] = test['Age'].fillna(-0, 5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]  # 구간
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        age_title_mapping = {0: 'Unknown', 1: 'Baby', 2: 'Child', 3: 'Teenager', 4: 'Student', 5: 'Young Adult',
                             6: 'Adult', 7: 'Senior'}
        for i in train, test:
            i['AgeGroup'] = pd.cut(train['Age'], bins=bins, labels=labels)
            i['AgeGroup'] = i['AgeGroup'].map(age_title_mapping)

        return this

    @staticmethod
    def accuracy_by_svm(this):
        score = cross_val_score(SVC())
