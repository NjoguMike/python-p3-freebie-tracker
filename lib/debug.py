# !/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session  = Session()
    import ipdb; ipdb.set_trace()

# engine = create_engine('sqlite:///freebies.db')


# dev1 = Dev(name="Michael")
# session.add(dev1)
# session.commit()


# company1 = Company("The star", 2022)
# session.add(company1)
# session.commit()

# freebie1 = Freebie(item_name="hat",value=10,dev_id=dev1.id,company_id=company1.id)
# session.add(freebie1)
# session.commit()

# Script goes here!
# print(dev1)
# print(company1)
# print(dev1.freebies)
# print(dev1.companies)
# print(company1.freebies)
# print(company1.devs)
# print(freebie1.dev)
# print(freebie1.company)