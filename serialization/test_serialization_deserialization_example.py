from typing import Optional
import json
from hypothesis import given, strategies as st


class User:
    def __init__(self, name: str, age: int, email: str, address: Optional[str] = None):
        self.name = name
        self.age = age
        self.email = email
        self.address = address

    def __eq__(self, other):
        if isinstance(other, User):
            return self.__dict__ == other.__dict__
        return False

    def __repr__(self):
        return f"User(name={self.name}, age={self.age}, email={self.email}, address={self.address})"


class UserSerializer:
    @staticmethod
    def to_json(user: User) -> str:
        return json.dumps(user)

    @staticmethod
    def from_json(data: str) -> User:
        json_data = json.loads(data)
        return User(**json_data)


user_strategy = st.builds(
    User,
    name=st.text(min_size=1),
    age=st.integers(min_value=0, max_value=120),
    email=st.emails(),
    address=st.one_of(st.none(), st.text(min_size=1))
)


# Define the property-based test
@given(user_strategy)
def test_user_json_serialization(user):
    serialized = UserSerializer.to_json(user)
    deserialized = UserSerializer.from_json(serialized)
    assert user == deserialized  # inverse property


# Running the property-based test
test_user_json_serialization()
