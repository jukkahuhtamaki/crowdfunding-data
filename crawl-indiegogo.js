/***
* Collecting Indiegogo crowd funding data.
***/
/*jshint strict:false*/
/*global CasperError, console, phantom, require*/ 
var casper = require('casper').create({
  verbose: true,
  clientScripts: ['includes/jquery-2.1.3.js'] 
});
var fs = require('fs');
var clicks = 0;
var x = require('casper').selectXPath; casper.start('https://www.indiegogo.com/projects/ jolla-tablet-world-s-first-crowdsourced-tablet #/funders');

function clickAndSave() {
  fs.write('data/01-raw/temp.html', this.getHTML('html'), 'w');
  // http://www.codigomanso.com/en/2010/07/simple- javascript-formatting-zero-padding/
  console.log('Click #' + clicks); 
  this.click(x("//a[text()='show more']")); 
  clicks += 1; 
  fs.write('data/01-raw/investments-sondor-click' + ('00000' + clicks).slice (-5) + '.html', this.getHTML('desktop-funders'), 'w');
  this.wait(1000*10, function() {});
  this.run(clickAndSave); 
}
casper.run(clickAndSave);