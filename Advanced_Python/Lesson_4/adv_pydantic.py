##### Pydantic #####

## Questions

# 1. What is Pydantic?
# 2. Why use Pydantic?
# 3. When to use Pydantic?
# 4. How to use Pydantic?

## Answers

# 1. Pydantic is a Python library that allows us to validate data. It is not a part of the Python standard library, so we need to install it. pip install pydantic
# 2. Pydantic is useful when we want to validate data. It is also useful when we want to serialize and deserialize data. It is also useful when we want to convert data to JSON. 
# It is also useful when we want to convert data to a dictionary, tuple, or list.
# 3. When we want to validate data, serialize and deserialize data, convert data to JSON, or convert data to a dictionary, tuple, or list.
# 4. We can use the BaseModel class to create a model. We can then use the model's methods to validate data, serialize and deserialize data, convert data to JSON, or convert data to a dictionary, tuple, or list.


## When and how projects use Pydantic?
# Pydantic is used in many projects. It is used in FastAPI, which is a Python web framework. It is also used in SQLAlchemy, which is an ORM. It is also used in Django, which is a Python web framework.
# Such projects use Pydantic to validate data, serialize and deserialize data, convert data to JSON, or convert data to a dictionary, tuple, or list.
# Examples of projects that use Pydantic:
#
# FastAPI: https://fastapi.tiangolo.com/
# SQLAlchemy: https://www.sqlalchemy.org/
# Django: https://www.djangoproject.com/


## Examples 

from pydantic import BaseModel, validator, root_validator, Field, ValidationError
from typing import List, Optional


class User(BaseModel):
    id: int = Field(alias='id', title='User ID', description='User ID')
    username = 'Davron_Dev'
    password: str
    password2: str
    age: int
    score: float
    email: Optional[str] = None
    phone: Optional[str] = None
    friends: List[int] = []

    def user_info(self):
        return f'User {self.username} is {self.age} years old'

    @validator('username')
    @classmethod
    def username_valid(cls, value):
        if not value.isalnum():
            raise ValueError('Username must be alphanumeric')
        return value

    @root_validator(pre=True) # pre=True means that the validator will be executed before the other validators.
    @classmethod
    def password_valid(cls, values):
        if values.get('password') != values.get('password2'):
            raise ValueError('Password must be the same as password2')
        return values

    class Config:
        '''Config class is used to configure the model.'''
        orm_mode = True # If True, the model can be used with ORMs such as SQLAlchemy and Django.
        allow_population_by_field_name = True # If True, the model can be initialized using field names.
        allow_mutation = False # If True, the model can be mutated.
        extra = 'ignore' # If 'forbid', extra fields will raise a validation error. If 'ignore', extra fields will be ignored. If 'allow', extra fields will be allowed.
        validate_assignment = True # If True, the model will be validated when assigning values to fields.
        validate_all = True # If True, the model will be validated when calling the validate() method.
        anystr_strip_whitespace = True # If True, all str fields will be stripped of whitespace before validation.
        anystr_lower = True # If True, all str fields will be lowercased before validation.


user = User(id=1, username='DavronDev', password = '123456', password2 = '123456', age=20, score=100.0, email='admin@gmail.com', phone='998977777777', friends=[2,3,4])

print(user)
print(user.id)

print(user.user_info())


########## Load data from JSON ##########
import json

json_users = [User(**user) for user in json.loads(open('user_data.json').read())]

for user in json_users:
    print(f'User from JSON: {user}')


########## Deserialize data ##########

users = User.parse_obj({'id': 1, 'username': 'DavronDev', 'password': '123456', 'password2': '123456', 'age': 20, 'score': 100.0, 'email': 'admin@gmail.com', 'phone': '998977777777', 'friends': [2,3,4]})
print(f'users Deserialize: {users}')

# parse_obj() method can be used to deserialize data from a dictionary.

########## Pydantic Parameters ##########

# 1. Field Parameters
# 2. Config Parameters

# 1. Field Parameters

# alias parameter (default=None) - The name of the field in the JSON response.
# Example: class User(BaseModel): id: int = Field(alias='user_id')

# title parameter (default=None) - The title of the field.
# Example: class User(BaseModel): id: int = Field(title='User ID')

# description parameter (default=None) - The description of the field.
# Example: class User(BaseModel): id: int = Field(description='User ID')

# default parameter (default=...) - The default value of the field.
# Example: class User(BaseModel): id: int = Field(default=1)

# default_factory parameter (default=...) - The default value of the field.
# Example: class User(BaseModel): id: int = Field(default_factory=lambda: 1)

# gt parameter (default=None) - The value of the field must be greater than the value of the gt parameter.
# Example: class User(BaseModel): id: int = Field(gt=0)

# ge parameter (default=None) - The value of the field must be greater than or equal to the value of the ge parameter.
# Example: class User(BaseModel): id: int = Field(ge=0)

# lt parameter (default=None) - The value of the field must be less than the value of the lt parameter.
# Example: class User(BaseModel): id: int = Field(lt=100)

# le parameter (default=None) - The value of the field must be less than or equal to the value of the le parameter.
# Example: class User(BaseModel): id: int = Field(le=100)

# max_length parameter (default=None) - The maximum length of the field.
# Example: class User(BaseModel): id: int = Field(max_length=100)

# min_length parameter (default=None) - The minimum length of the field.
# Example: class User(BaseModel): id: int = Field(min_length=1)

# regex parameter (default=None) - The regex of the field.
# Example: class User(BaseModel): id: int = Field(regex='[a-z]+')


# 2. Config Parameters

# orm_mode parameter (default=False) - If True, the model can be used with ORMs such as SQLAlchemy and Django.
# Example: class Config: orm_mode = True 

# allow_population_by_field_name parameter (default=False) - If True, the model can be initialized using field names.
# Example: class Config: allow_population_by_field_name = True

# allow_mutation parameter (default=True) - If True, the model can be mutated.
# Example: class Config: allow_mutation = False

# extra parameter (default='forbid') - If 'forbid', extra fields will raise a validation error. If 'ignore', extra fields will be ignored. If 'allow', extra fields will be allowed.
# Example: class Config: extra = 'ignore'

# validate_assignment parameter (default=True) - If True, the model will be validated when assigning values to fields.
# Example: class Config: validate_assignment = True

# validate_all parameter (default=False) - If True, the model will be validated when calling the validate() method.
# Example: class Config: validate_all = True

# anystr_strip_whitespace parameter (default=False) - If True, all str fields will be stripped of whitespace before validation.
# Example: class Config: anystr_strip_whitespace = True

# anystr_lower parameter (default=False) - If True, all str fields will be lowercased before validation.
# Example: class Config: anystr_lower = True

# arbitrary_types_allowed parameter (default=False) - If True, arbitrary types will be allowed.
# Example: class Config: arbitrary_types_allowed = True

# json_encoders parameter (default={}) - A dict of custom JSON encoders.
# Example: class Config: json_encoders = {datetime: lambda dt: dt.isoformat()}

# use_enum_values parameter (default=False) - If True, enum values will be used instead of enum names.
# Example: class Config: use_enum_values = True

# fields parameter (default={}) - A dict of custom field definitions.
# Example: class Config: fields = {'id': {'alias': 'user_id'}}




############################################ @dataclass vs Pydantic ############################################

# @dataclass vs Pydantic

# @dataclass is a decorator that is used to create a data class. A data class is a class that is used to store data.
# Pydantic is a library that is used to validate data. Pydantic is used to create data models.

# Performance

# @dataclass is faster than Pydantic because @dataclass is a built-in decorator and Pydantic is a third-party library.

# Validation

# @dataclass does not validate data. Pydantic validates data.

# Type Hinting

# @dataclass does not support type hinting. Pydantic supports type hinting. Pydantic uses type hinting to validate data. Pydantic also uses type hinting to generate documentation. Pydantic also uses type hinting to generate JSON schemas.



############################################ Class data alternatives ############################################

# Class data alternatives

# 1. NamedTuple
# 2. TypedDict
# 3. dataclasses.dataclass
# 4. attrs.attrs
# 5. pydantic.BaseModel

# 1. NamedTuple

# NamedTuple is a tuple with named fields. NamedTuple is a subclass of tuple. NamedTuple is immutable. NamedTuple is faster than a regular tuple. NamedTuple is faster than a regular class. NamedTuple is faster than a regular class with __slots__. 

# 2. TypedDict

# TypedDict is a dictionary with typed fields. TypedDict is a subclass of dict. TypedDict is mutable. TypedDict is faster than a regular dictionary. TypedDict is faster than a regular class. TypedDict is faster than a regular class with __slots__.

# 3. dataclasses.dataclass

# dataclasses.dataclass is a decorator that is used to create a data class. A data class is a class that is used to store data. dataclasses.dataclass is a subclass of object. dataclasses.dataclass is mutable. dataclasses.dataclass is slower than a regular class. dataclasses.dataclass is slower than a regular class with __slots__.

# 4. attrs.attrs

# attrs.attrs is a decorator that is used to create a class. attrs.attrs is a subclass of object. attrs.attrs is mutable. attrs.attrs is slower than a regular class. attrs.attrs is slower than a regular class with __slots__

# 5. pydantic.BaseModel

# pydantic.BaseModel is a class that is used to create data models. pydantic.BaseModel is a subclass of object. pydantic.BaseModel is mutable. pydantic.BaseModel is slower than a regular class. pydantic.BaseModel is slower than a regular class with __slots__.


# What is the best class data alternative?

# The best class data alternative is a regular class with __slots__. 

