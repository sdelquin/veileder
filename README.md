# Veileder

*Veileder* is the norwegian translation of "supervisor". I am not norwegian, but it sounds fine 😉.

This tool checks if `supervisord` is running, and if not, it notifies you through sending an email. Let's say that it is a supervisor of supervisor. Recursive?? 🤔 hehe

## Cron

It would be interesting to set a cron job in order to periodically check if supervisord is running. Here you have an example of a cron entry, where the checking is done every 30 minutes:

~~~bash
*/30 * * * * $HOME/veileder/run.sh > $HOME/logs/veileder.log 2>&1
~~~
