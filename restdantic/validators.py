from typing import Any

from pydantic_core.core_schema import ValidationInfo


def validate_lookup_related_field(cls, value: Any, info: ValidationInfo):
    json_schema_extra = cls.model_fields[info.field_name].json_schema_extra
    queryset = json_schema_extra['queryset']
    lookup_field = json_schema_extra['lookup']
    many = "list" in str(cls.model_fields[info.field_name].annotation)

    if many:
        if not isinstance(value, list):
            raise TypeError(f"Invalid type. Expected list, got {type(value).__name__}.")
        if not all(isinstance(v, int) for v in value):
            raise TypeError(f"Invalid type. Expected list of ints, got {type(value).__name__}.")
        filter_kwargs = {f'{lookup_field}__in': value}
    else:
        if not isinstance(value, int):
            raise TypeError(f"Invalid type. Expected int, got {type(value).__name__}.")
        filter_kwargs = {lookup_field: value}

    try:
        objects = queryset.filter(**filter_kwargs)
        if many:
            if len(objects) != len(value):
                object_values = set(getattr(obj, lookup_field) for obj in objects)
                invalid_values = set(value) - object_values
                raise ValueError(f"Invalid {lookup_field}(s) {invalid_values} - object(s) do not exist.")
            return list(objects)
        else:
            return objects.get()
    except queryset.model.DoesNotExist:
        raise ValueError(f'Invalid {lookup_field} "{value}" - object does not exist.')
    except TypeError:
        raise TypeError(f"Invalid type. Expected int or list, got {type(value).__name__}.")
