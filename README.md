# Integrating Telemetry into GA4GH API-powered federated microservice networks

The Global Alliance for Genomics and Health (GA4GH) defines various web APIs for federated computing solutions that are well suited for the microservice architecture pattern. The ELIXIR Cloud & AAI Driver Project of the GA4GH is actively developing a GA4GH API-powered cloud environment based on this principle.
The GA4GH Cloud Telemetry Project aims to provide a starting point for instrumentation and tracing of GA4GH Cloud Components / Microservices. 

In this project, you would design and implement a solution that adds rich telemetry support to the ELIXIR Cloud federated service. The primary goal would be deployment artifacts (e.g., Terraform/OpenTofu) that deploy both our core services, as well as telemetry services at our fragmented compute centers at multiple locations (Kubernetes, OpenShift, OpenStack/VMs), as well as on one or more commercial cloud providers.
An ideal solution would be easily extensible to apply to GA4GH-powered clouds in general, i.e., proposals that use abstractions offered by GA4GH APIs, where applicable/reasonable, are preferred.

A simple telemetry sidecar deployment might be a reasonable aim for a short project, whereas a generic solution with various connections to specific GA4GH APIs (e.g., integration with the Service Info / Service Registry API) might be suitable for a medium or even long project. Note that the exclusive use of free and open source tooling for any used dependencies (e.g., OpenTelemetry) is a requirement.

## Organization

* [Issues](https://github.com/elixir-cloud-aai/cloud-telemetry/issues)
* [Project Board](https://github.com/orgs/elixir-cloud-aai/projects/21)
* Communication: ELIXIR Cloud Slack Channel, Topic #telemetry

