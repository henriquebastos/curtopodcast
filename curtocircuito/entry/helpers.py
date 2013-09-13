# coding: utf-8


def drop_field(model, name):
    '''Remove a local_field from an abstract model.'''
    meta = model._meta
    assert meta.abstract

    removed = False # Monitors if a field was removed

    for i, f in enumerate(meta.local_fields):
        if f.name == name:
            meta.local_fields.pop(i)
            removed = True

    # Clear cache
    if removed:
        if hasattr(meta, '_field_cache'):
            del meta._field_cache
            del meta._field_name_cache

        if hasattr(meta, '_name_map'):
            del meta._name_map

