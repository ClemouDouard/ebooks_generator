<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h1 align="center">Ebooks generator</h1>

  <p align="center">
    A complete ebook generator powered by AI.
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
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
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is built to make the process of creating ebooks easier and faster.
This is powered by the Mistral AI API, using crewAI to manage the agents and tasks.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With


* [![Mistral][Mistral]][Mistral-url]
* [![Streamlit][Streamlit]][Streamlit-url]
* [![CrewAI][CrewAI]][CrewAI-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

  ```sh
  python3.12 -m venv venv
  source venv/bin/activate
  ```

### Installation

1. Get a free API Key at [Mistral](https://console.mistral.ai/api-keys)
2. Clone the repo
   ```sh
   git clone https://github.com/ClemouDouard/ebooks_generator.git
   ```
3. Install packages
   ```sh
   pip install -r requirements.txt
   ```
4. Create a `src/config.py` file and enter your API key as well as your LLM model
   ```sh
   cd src
   touch config.py
   echo "API_KEY = 'ENTER YOUR API'" >> config.py
   echo "MODEL = 'ENTER YOUR MODEL'" >> config.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Work in progress

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Structure
- [ ] Ideas
- [ ] Content
- [ ] Interface

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/ClemouDouard/ebooks_generator/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ClemouDouard/ebooks_generator" alt="contrib.rocks image" />
</a>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/ClemouDouard/ebooks_generator](https://github.com/ClemouDouard/ebooks_generator)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ClemouDouard/ebooks_generator.svg?style=for-the-badge
[contributors-url]: https://github.com/ClemouDouard/ebooks_generator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ClemouDouard/ebooks_generator.svg?style=for-the-badge
[forks-url]: https://github.com/ClemouDouard/ebooks_generator/network/members
[stars-shield]: https://img.shields.io/github/stars/ClemouDouard/ebooks_generator.svg?style=for-the-badge
[stars-url]: https://github.com/ClemouDouard/ebooks_generator/stargazers
[issues-shield]: https://img.shields.io/github/issues/ClemouDouard/ebooks_generator.svg?style=for-the-badge
[issues-url]: https://github.com/ClemouDouard/ebooks_generator/issues
[license-shield]: https://img.shields.io/github/license/ClemouDouard/ebooks_generator.svg?style=for-the-badge
[license-url]: https://github.com/ClemouDouard/ebooks_generator/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/clementleveque
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[Streamlit-url]: https://streamlit.io/
[Streamlit]: https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white
[CrewAI-url]: https://www.crewai.com/
[CrewAI]: https://img.shields.io/badge/CrewAI-000000?style=for-the-badge&logo=CrewAI&logoColor=white
[Mistral-url]: https://mistral.ai/
[Mistral]: https://img.shields.io/badge/Mistral-000000?style=for-the-badge&logo=Mistral&logoColor=white