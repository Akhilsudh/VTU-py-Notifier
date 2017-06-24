# VTU-py-Notifier

Fed up of checking the VTU website for your results everyday??? Use this script and chill, till this devil of a script notifies you about it :P
-------------------
Requirements:
-------------------
* Install pip by downloading the 'get-pip.py' from: https://bootstrap.pypa.io/get-pip.py ,and running the following command:
  
  ` $ python get-pip.py`

* Install BeautifulSoup, which is used for parsing the website's HTML, by running the following command:
  
  ` $ apt-get install python-bs4`

* Install twilio module, which is the service used to send the SMS, by running the following command:
  
  ` $ pip install twilio`

------------------
How To Use:
------------------
>This script uses command line arguements to take in 6 values :
  * VTU University Seat Number
  * Account SID for Twilio
  * Auth Token for Twilio
  * Your Twilio Phone Number
  * To Phone Number

>For example the command would look like this :
  * `$ python RESULTS.py <USN> <Twilio Account SID> <Twilio Auth Token> "<Your Twilio Phone Number>" "<To Phone Number>"`
  * `$ python RESULTS.py 1ab1234567 #####86d3ea#######07030366f####### #####d9e6#######eb504e18b####### "+# ###-###-####" "+# ###-###-####"`*

>To run the above script periodically, use *CronTab* to do the job and you are good to go   


## License
    The MIT License (MIT)

    Copyright (c) 2014-2016 Akhil Sudhakaran
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
  
*The example used here is for representational use only. Please replace it with your parameter values.  
