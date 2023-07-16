from pydantic import BaseModel as PydanticBaseModel
from pydantic import field_validator
from pydantic.fields import FieldInfo
from pydantic.main import ModelMetaclass as PydanticModelMetaclass

from restdantic.validators import validate_lookup_related_field


class BaseModelMeta(PydanticModelMetaclass):
    """
    Extends the Pydantic ModelMetaclass to add additional attributes
    to the class during creation.

    This metaclass is used to implement additional validation for related lookup fields.
    For each attribute in the class that has a FieldInfo instance
    as its value and its `json_schema_extra` property has 'is_related_lookup' as True,
    a new validation method is added to the class.

    The new method is added before the class is created, allowing it to be used in the same
    way as built-in validation methods.
    """
    def __new__(mcls, name, bases, attrs):
        additional_attrs = {}
        for attr_name, attr in attrs.items():
            if isinstance(attr, FieldInfo):
                json_schema_extra = attr.json_schema_extra or {}
                if json_schema_extra.get('is_related_lookup'):
                    additional_attrs[f'validate_{attr_name}'] = field_validator(
                        attr_name, mode='before'
                    )(validate_lookup_related_field)
        attrs.update(additional_attrs)
        return super().__new__(mcls, name, bases, attrs)


class BaseModel(PydanticBaseModel, metaclass=BaseModelMeta):
    model_config = {
        'arbitrary_types_allowed': True,
    }
