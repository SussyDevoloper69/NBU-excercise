# NBU-excercise
Docker compose floodlight/mininet
# assignment
The end-of-semester exercise is
- Install docker and familiarize yourself with it according to docker-ciriculum;
- Familiarize yourself with docker compose and have the ability to compose your application stack into containers;

- Meet mininet;

- Familiarize yourself with the SDN controller floodlight;

- Make a repo on github

- Write an example mininet python script that creates a network with a topology of <XYZ> switch and <YX> host connected in the topology of your observation.

X - the penultimate digit of your faculty number;
Y - the first digit of your faculty number;
Z - the last digit of your faculty number;
- Make your own docker-compose setup in the repo that contains:

mininet
floodlight
Your script
Demonstrate how to configure two-way traffic rules between the two furthest hosts on your network with a script to the floodlight API.

Demonstrate that your script works by pinging between the two hosts you created the rules for.

Send me a screen recording on youtube demonstrating the essence of your setup and a link to your repo.
# About the university
-New Bulgarian University
-Tutor: Mr.Nikolay Milovanov
-Course: Telecommunications and computer technologies

# How to run 
1. docker pull iwaseyusuke/mininet
2. git clone http://github.com/SussyDevoloper69/NBU-excercise/main/
3. cd project/
4. docker build -t floodlight-imagev2 .
5. docker compose up
6. chmod +x ./automate.sh
7. ./automate.sh
# Link to youtube
