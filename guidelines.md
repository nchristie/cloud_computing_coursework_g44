Source: https://qmplus.qmul.ac.uk/mod/page/view.php?id=1537755

# MINI PROJECT GUIDELINES
## INTRODUCTION


The goal of the mini-project is to apply and extend the techniques practised during the labs, in order to build a prototype of a Cloud application.

The project will have the form of an application, developed in Python and Flask. You can choose to use a different programming language and application server if you have experience with them.

The mini project will work on the following aspects of Cloud applications: (10 points)

- [x] REST-based service interface for CRUD operations (for example: data query and post-processing).
- [x] Interaction with external REST services. (please see Additional Information)
- [ ] Use of an external Cloud database for persisting information. (for example: any database server of GCP, AWS, other providers like MS Azure, Heroku (no credits required).

## PROJECT SPECIFICATION

You can decide the application domain for your application. You can either build your application on top of the examples we developed during the labs, or select a different domain for it.

The base application to be developed has a base score of 10/15 points, as long as it complies with the following requirements:

- [x] The application provides a dynamically generated REST API. The API must have a sufficient set of services for the selected application domain. The REST API responses must conform to REST standards (e.g. response codes).  3 Points
- [x] The application makes use of an external REST service to complement its functionality. 3 Points
- [ ] The application uses a cloud database for accessing persistent information. 3 Points
- [ ] The application code is well documented (in each of the code files, as well as in the README.MD file of the git repository). 1 Point

In addition to that, mini projects can do additional tasks to get up to 5 points by implementing additional features such as the ones discussed here. These might require students to research specific techniques beyond what has been covered in the labs (either of the three options below):

- [ ] Option 1: 5 points for demonstration of load balancing/scaling of the application (e.g. Kubernetes based load balancing/GKE). In order to get the full 5 marks, the student must demonstrate (in the video presentation) the effect in practice of these techniques.

- [ ] Option 2: Up to 5 for any 3 implementations as mentioned below  :

  - [ ] Serving the application over https.
  - [ ] Implementing hash-based authentication.
  - [ ] Implementing user accounts and access management.
  - [ ] Securing the database with role-based policies.

- [ ] Option 3: Up to 5 points: Anything else that would be relevant to a cloud application (needs to be pre-approved by Sukhpal - contact through email first).

SUBMISSION AND ASSESSMENT

- [x] Submission: You should use a git repository to deploy your code. You can either use a public github url, or have a private repo from QMUL ITS Research github repository.

Assessment: The project will be scored over 15 points, and will be worth 15% of your final mark.

- [ ] You will need to upload the recorded video on YouTube. You must be able to explain what your application is doing, and how. Every project must be demonstrated in order for it to be assessed.

- [ ] In the submission page you only have to provide links to the git repository and YouTube video.

Whenever your project is examined, you will receive a grade, and feedback.

ADDITIONAL INFORMATION

In order to provide ideas for application domains for the mini project, we encourage students to look at available public REST APIs. Some potentially useful REST APIs for ideas can be found at https://github.com/public-apis/public-apis