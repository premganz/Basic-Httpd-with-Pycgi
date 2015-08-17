# Interop-Java-Groovy-Python

The idea is to demonstrate how to interoperate three languages which have their own strenghts.
Java as the mainstream programming language and ability to build complex applications.

Python has as one of its strengths the ability to work closely with native code with its CTypes library.
Groovy is very strong in text content templating.

Of course welding these together requires external dependencies. 
Here I would need activemq and apache httpd. The integration of java with python would be through cgi script invocation via python from a httpClient.
For groovy it would be an mq based interaction.
I am including the associated resources like httpd.conf example in the resources for reference while setting up the dependencies. 

Of course you will need to install Python in your machine. 2.7 preferred. 

