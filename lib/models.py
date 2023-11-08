from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Table, func
from sqlalchemy.orm import relationship, backref, declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base()

dev_company = Table(
    'dev_companies',
    Base.metadata,
    Column('dev_id', ForeignKey('devs.id'), primary_key=True),
    Column('company_id', ForeignKey('companies.id'), primary_key=True),
    extend_existing=True
)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    freebies = relationship('Freebie', back_populates='company')
    devs = relationship('Dev', secondary=dev_company, back_populates='companies')

    def give_freebie(self,dev, item_name, value):
        freebie = Freebie(item_name=item_name, value=value, dev_id=dev.id,company_id=self.id)
        return freebie
    
    def oldest_company(self):
        company_years = []
        company_years.append(self.founding_year)
        pass

    def __repr__(self):
        return f'<Company {self.name}>'

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    freebies = relationship('Freebie', back_populates='dev')
    companies = relationship('Company', secondary=dev_company, back_populates='devs')

    def __repr__(self):
        return f'<Dev {self.name}>'

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())
    dev_id = Column(Integer(), ForeignKey('devs.id'))
    company_id = Column(Integer(), ForeignKey('companies.id'))

    company = relationship('Company', back_populates='freebies')
    dev = relationship('Dev', back_populates='freebies')

    def print_details(self):
        return f'{self.dev} owns a {self.item_name} from {self.company}'

    def __repr__(self):
        return f'<Dev item_name={self.item_name}, value={self.value}>'