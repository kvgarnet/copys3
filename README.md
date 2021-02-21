


<p align="center">
  
  <h3 align="center">CopyS3</h3>

  </p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## What is CopyS3
It is a Docker containerized Python application. 
When given the names of two S3 buckets (source, destination) and a threshold size (in MB), application will copy
all files greater than the specified threshold size from the source bucket to the destination bucket.
Assumptions are that the buckets are in the same region.


<!-- GETTING STARTED -->
## Getting Started

The application is built with AWS python SDK boto3 module, interacting with AWS S3 service

### Prerequisites
- A Linux host server for below tools installation
- [AWS Account](https://aws.amazon.com/free/?nc2=h_ql_pr) - free tier can be utilized for this exercise since all we need are (2) S3 buckets
  - [AWS CLI ](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html)
- [Docker](https://docs.docker.com/install/)  - Install latest docker for your operating system.
- [Python](https://www.python.org)  - please use Python 3.6.x or greater if you decide to use Python
  - [AWS SDK Python boto3](https://aws.amazon.com/sdk-for-python/) - ensure boto3 installed on host server
- Create IAM user with AWSS3fullaccess permission. record user's AK/SK credentials
- Configure AK/SK via 'aws configure' on host server
- Verify that aws cli tool can work with S3, create S3 buckets as below:

**Note:replace bucket names with your own**
```sh
aws s3 mb s3://kvsource
aws s3 mb s3://kvdest
aws s3 ls
```



### Installation
After above prerequisites tools installed on Linux Servers, please configure docker images as below:

1. Clone the repo
   ```sh
   git clone https://github.com/kvgarnet/copys3.git
   ```
2. Build Docker Image
   ```sh
   make build 
   ```
3. Generate files with different sizes to source bucket via aws cli
```
make 
```
4. Upload files with different sizes to source bucket via aws cli
```
make upload 
#by default it will use my account's source bucket 'kvsource', can also set your bucket name with:
make upload  source=<your_bucket>
```

## Usage
### Test apllication locally
1. Before running the docker container, you can also run python application locally
```
copys3.py <sourcebucket> <destinationbucket> <threshold>
# in my AWS test account, example as
copys3.py kvsource kvdest 3
```
2. Verify to see files were copied to kvdest bucket:
```sh
 aws s3 ls s3://kvdest
```

### Run the docker application

1. Run the application:
<br/>
1.1  use the 3MB as default threshold,copy files from 'kvsource' to 'kvdest'
   ```sh
  make run
```
<br/>
1.2 use the 1MB as size threshold,copy files from 'frombucket' to ' tobucket'
```sh
make run source=kvsource dest=kvdest size=1
```



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
