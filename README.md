#my_modules

First module "time_formating".
This module takes time in seconds and return it in a human readable way.
this module was my answer for a kata on codewars website.

You can see this kata on this link "https://www.codewars.com/kata/human-readable-duration-format/"

The function must accept a non-negative integer. 
If it is zero, it just returns "now". 
Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

Format_duration(62)    # returns "1 minute and 2 seconds".
Format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds".

For the purpose of this Kata, a year is 365 days and a day is 24 hours.
Note that spaces are important.

Detailed rules:

The resulting expression is made of components like 4 seconds, 1 year, etc. 
In general, a positive integer and one of the valid units of time, separated by a space. 
The unit of time is used in plural if the integer is greater than 1.
The components are separated by a comma and a space (", "). 
Except the last component, which is separated by " and ", just like it would be written in English.
A more significant units of time will occur before than a least significant one. 
Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.
Different components have different unit of times. 
So there is not repeated units like in 5 seconds and 1 second.
A component will not appear at all if its value happens to be zero. 
Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.
A unit of time must be used "as much as possible". 
It means that the function should not return 61 seconds, but 1 minute and 1 second instead. 
Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

Second module "DaysBetweenDates".

This module takes two dates and return number of days between them.
Module can deal with leap years and curious case of month feb.
Also it can check that date two is after date one and this is very important.

Third module "measure time to execute".

This module calculate time to run a method or Whole code in seconds.

Forth module "play in wordlists".

This module can talk any wordlist and count specified length passwords.
I will work on this module to give it ability to talk this specified length passwords to another file.

Fifth module "renameFiles".

This module can go to specific path and rename all files in this folder.
