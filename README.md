#  Get your head in the cloud - Accenture Webinar@ASMI 2020
#### The POC  developed for Accenture's webinar held at an [online event](https://ro-ro.facebook.com/events/403881667404041/) organized by [ASMI](https://www.asmi.ro/)
#### The project consists of multiple modules that leverage AWS to detect a cat and track its eating habits   

#### The implementation is a PoC and should be treated as such, but if you find something *fishy*, feel free to contribute and correct it!

## Modules
- [observer](./cat_detector/observer/README.md) - a thin module that produces a continuous stream of pictures uploaded in the cloud

- [collector](./cat_detector/collector/README.md) - a web API that analyzes photos and exposes the results through multiple HTTP endpoints

- [dashboard](./cat_detector/dashboard/README.md) - a web interface that consumes information from the `collector` module and exposes it as a chart