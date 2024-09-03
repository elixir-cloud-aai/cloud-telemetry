[![Bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://bandit.readthedocs.io/en/latest/)
[![codecov](https://codecov.io/gh/elixir-cloud-aai/cloud-telemetry/branch/main/graph/badge.svg)](https://codecov.io/gh/elixir-cloud-aai/cloud-telemetry)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)][code-of-conduct]
[![Documentation Status](https://readthedocs.org/projects/cloud_telemetry/badge/?version=latest)](https://cloud_telemetry.readthedocs.io/en/latest/?badge=latest)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](./LICENSE)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![GitHub contributors](https://img.shields.io/github/contributors/elixir-cloud-aai/cloud-telemetry)](https://github.com/elixir-cloud-aai/cloud-telemetry/graphs/contributors)
[![Ruff](https://img.shields.io/badge/linter%20&%20formatter-ruff-000000.svg)](https://docs.astral.sh/ruff/)
[![Safety](https://img.shields.io/badge/security-safety-orange.svg)](https://safetycli.com/product/safety-cli)

# Integrating Telemetry into GA4GH API-powered federated microservice networks

The Global Alliance for Genomics and Health (GA4GH) defines various web APIs for
federated computing solutions that are well suited for the microservice
architecture pattern. The ELIXIR Cloud & AAI Driver Project of the GA4GH is
actively developing a GA4GH API-powered cloud environment based on this
principle. The GA4GH Cloud Telemetry Project aims to provide a starting point
for instrumentation and tracing of GA4GH Cloud Components / Microservices.

In this project, you would design and implement a solution that adds rich
telemetry support to the ELIXIR Cloud federated service. The primary goal would
be deployment artifacts (e.g., Terraform/OpenTofu) that deploy both our core
services, as well as telemetry services at our fragmented compute centers at
multiple locations (Kubernetes, OpenShift, OpenStack/VMs), as well as on one or
more commercial cloud providers. An ideal solution would be easily extensible to
apply to GA4GH-powered clouds in general, i.e., proposals that use abstractions
offered by GA4GH APIs, where applicable/reasonable, are preferred.

A simple telemetry sidecar deployment might be a reasonable aim for a short
project, whereas a generic solution with various connections to specific GA4GH
APIs (e.g., integration with the Service Info / Service Registry API) might be
suitable for a medium or even long project. Note that the exclusive use of free
and open source tooling for any used dependencies (e.g., OpenTelemetry) is a
requirement.

## Table of Contents

- [Basic Usage](#basic-usage)
- [Installation](#installation)
- [Development](#development)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [Versioning](#versioning)
- [License](#license)
- [Contact](#contact)

## Basic Usage

## Installation

## Development

For ease of use, certain scripts have been abbreviated in `Makefile`, make sure
that you have installed the dependencies before running the commands.

> **Note**: `make` commands are only available for Unix-based systems.

To view the commands available, run:

```sh
make
```

Here are certain commands that you might find useful:

- Make a virtual environment

```sh
make v
```

- Install all dependencies including optional dependencies

```sh
make i
```

> **Note**: This project uses optional dependency groups such as `types`,
> `code_quality`, `docs`, `vulnerability`, `test`, and `misc`. To install stubs
> or types for the dependencies, you **must** use the following command:
>
> ```sh
> poetry add types-foo --group types
> ```
>
> Replace `types-foo` with the name of the package for the types. All runtime
> dependencies should be added to the `default` group. For example, to install
> `requests` and its type stubs, run:
>
> ```sh
> poetry add requests
> poetry add types-requests --group types
> ```
>
> This ensures that the type checker functions correctly.
>
> **Note**: Since the dependencies are segregated into groups, if you add a new
> group make sure to add it in `make install` command in [Makefile](Makefile).

- Run tests

```sh
make t
```

- Run linter, formatter and spell checker

```sh
make fl
```

- Build the documentation

```sh
make d
```

> **Note**: If you make changes to the code, make sure to generate and push the
> documentation using above command, else the documentation check CI will fail.
> Do NOT edit auto-generated documentation manually.

- Run type checker

```sh
make tc
```

- Run all pre-commit checks

```sh
make pc
```

- Update the cookiecutter template

```sh
make u
```

> **Note**: This is not the complete list of commands, run `make` to find out if
> more have been added.

## Environment Variables

**Cloud-Telemetry supports all environment variables** **supported by the
OpenTelemetry SDK**

For a complete list, check
[here](https://opentelemetry-python.readthedocs.io/en/latest/sdk/environment_variables.html).

## Contributing

This project is a community effort and lives off _your_ contributions, be it in
the form of bug reports, feature requests, discussions, fixes or any other form
of contribution!

Please refer to the guidelines available at [`CONTRIBUTING.md`][contributing] if
you are interested in contributing.

## Code of Conduct

We kindly request all contributors to abide by our
[organization's Code of Conduct][code-of-conduct]. Please also refer to this
document if you want to report an incident with respect to conduct in our
community. Thank you for your cooperation.

## Versioning

The project adopts the [semantic versioning][semver] scheme for versioning.
Currently the software is in a pre-release stage, so changes to the API,
including breaking changes, may occur at any time without further notice.

## License

This project is distributed under the [Apache License 2.0][badge-license-url], a
copy of which is also available in [`LICENSE`][license].

## Contact

The project is maintained by [ELIXIR Cloud & AAI][elixir-cloud-aai], a Driver
Project of the [Global Alliance for Genomics and Health (GA4GH)][ga4gh], under
the umbrella of the [ELIXIR] [Compute Platform][elixir-compute].

To get in touch with us, please use one of the following routes:

- For filing bug reports, feature requests or other code-related issues, please
  make use of the project's [issue tracker][issue-tracker].
- For private/personal issues, more involved communication, or if you would like
  to join our team as a regular contributor, you can either join our
  [chat board][badge-chat-url] or [email] the community leaders.
- [Project Board](https://github.com/orgs/elixir-cloud-aai/projects/21)
- Communication: ELIXIR Cloud Slack Channel, Topic #telemetry

[![logo-elixir]][elixir] [![logo-elixir-cloud-aai]][elixir-cloud-aai]

[badge-chat-url]: https://join.slack.com/t/elixir-cloud/shared_invite/enQtNzA3NTQ5Mzg2NjQ3LTZjZGI1OGQ5ZTRiOTRkY2ExMGUxNmQyODAxMDdjM2EyZDQ1YWM0ZGFjOTJhNzg5NjE0YmJiZTZhZDVhOWE4MWM
[badge-license-url]: http://www.apache.org/licenses/LICENSE-2.0
[code-of-conduct]: https://elixir-cloud-aai.github.io/about/code-of-conduct/
[contributing]: https://elixir-cloud-aai.github.io/guides/guide-contributor/
[elixir]: https://elixir-europe.org/
[elixir-cloud-aai]: https://elixir-cloud.dcc.sib.swiss/
[elixir-compute]: https://elixir-europe.org/platforms/compute
[email]: mailto:cloud-service@elixir-europe.org
[ga4gh]: https://ga4gh.org/
[issue-tracker]: https://github.com/elixir-cloud-aai/cloud-telemetry/issues
[license]: LICENSE
[logo-elixir]: images/logo-elixir.svg
[logo-elixir-cloud-aai]: images/logo-elixir-cloud-aai.svg
[semver]: https://semver.org/
