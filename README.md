# pulumi_maas

A Pulumi package for creating and managing Canonical [Metal-As-A-Service](https://maas.io/) (MAAS) resources.

## Prerequisites

Before you begin, make sure you have the following prerequisites installed and configured:

```bash
pulumi new python
pulumi stack init dev
```

Install `pulumi-maas` Python 3 package:

```bash
pip install pulumi-maas
```

Export MaaS variables:

```bash
export MAAS_API_VERSION=2.0
export MAAS_API_KEY=xxxxxxxx
export MAAS_API_URL=http://maas.example.org:5240/MAAS
```

## Examples

### Create a new domain

```python
import pulumi
import pulumi_maas as maas

test_example_domain = maas.DnsDomain(
    "test_domain",
    name="test.example.org",
    ttl=3600,
    authoritative=True,
)

pulumi.export("test_example_domain", test_example_domain.id)
```

Launch Pulumi commands:

```bash
pulumi preview
pulumi up
pulumi destroy
```

## Contributing

Contributions to this project are welcome! If you find any issues or have improvements to suggest, please open an issue or submit a pull request.

## Acknowledgments

- Pulumi Documentation
- Metal as a Service (MaaS) Documentation

## Go further
### Publish this project

```bash
python3 setup.py sdist bdist_wheel
twine upload --repository pypi dist/*
```
