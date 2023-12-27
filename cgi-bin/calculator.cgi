#!C:/xammp/bin/perl.exe
use strict;
use warnings;

my $expression = $ENV{'QUERY_STRING'} || '';

my $result = calculate($expression);

print "Content-type: text/html\r\n\r\n";
print "<html><head><title>Resultado</title></head><body>";
print "<h2>Resultado:</h2><p>$result</p>";
print "</body></html>";

sub calculate {
    my ($expression) = @_;

