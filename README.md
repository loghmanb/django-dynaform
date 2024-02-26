# django-dynaform
Dynamic form for Django framework

![PyPI](https://img.shields.io/pypi/v/django-dynaform?label=django-dynaform)

## Overview

Dynamic Django forms allow users to define, edit, and populate their own entities and apply runtime schema changes to them. `django-dynaform` is a unique tools to empower your project with more dynamicity with minimum database changes. It is ideal and unique tools for frequently changing and/or temporary data structures. It is the goal of this project to provide a bring dynamicity with maximum benefit to a project with less effort.

This package provides models to help admin users quickly add/change/drop dynamic models for their specific use case, and use them in dynamic templates. The schema changes are applied in the runtime, *without* database metadata changes, so it could use in dynamic templates with zero downtime and any side effects of changing in data structure.

> **Disclaimer**:
> 
> It is not recommended to use this project for business critical data due to the high potential for data loss. Tables can be dropped very easily, and without backups, even a small user error could be catastrophic.

## Example project

You can download an example project from https://github.com/loghmanb/django-dynaform/example
go to the folder and run below commands

```shell
$ pip install -r requirements.txt
$ python manage.py loaddata sample-data.json.gz
$ python manage.py runserver 0:8000
```

## Documentation

See the [wiki](https://github.com/loghmanb/django-dynaform/wiki) for documentation.
