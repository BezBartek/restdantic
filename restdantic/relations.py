from typing import Any

from django.db.models import QuerySet
from pydantic import Field


def LookupRelatedField(  # noqa C901
    *, lookup: str, queryset: QuerySet, **kwargs
) -> Any:
    return Field(lookup=lookup, queryset=queryset, is_related_lookup=True, **kwargs)
