# Colab Tools/Wrappers

This repository contains some tools and wrappers to get started with Google Colab.

## Getting Started

Import this repository into your Google Colab environment and import drive_files class.
The class has helper functions to list files and download non-utf8 encoded files.

### Prerequisites

Install PyDrive before running any scripts.

```
!pip install -U -q PyDrive
```

### Installing

Clone this repository in your Colab VM:
```
git clone https://github.com/sushrutbhalla/ColabToolsWrappers.git
```

List all files in your Google Drive using:
```
from drive_files import drive_files
drive_f = drive_files()
drive_f.list_files()
```

<!--
## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 
-->

## Authors

* **Sushrut Bhalla** - *Initial work* - [sushrutbhalla](https://github.com/sushrutbhalla)

<!--
See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.
-->

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

<!--
## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
-->
