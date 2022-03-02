//Chapter 7: Strings
//Section 7.1: Basic Info and String Concatenation
var hello = "Hello";
var world = 'world';
var helloW = `Hello World`;

//using String() method
var intString = String(32); 
var booleanString = String(true); 
var nullString = String(null);

//using toString() method
var intString = (5232).toString(); 
var booleanString = (false).toString(); 
var objString = ({}).toString();


//using String.fromCharCode
String.fromCharCode(104,101,108,108,111);
//prints "hello"

//using new keyword
var objectString = new String("Yes, I am a String object");
typeof objectString;//work as object
typeof objectString.valueOf();//"string"

//String Concatenation
var name = "Harshita";
var sname = "Tandale";
console.log(name + sname); 
console.log(name + " " + sname);
name.concat(sname);
"a".concat("b", " ", "d");

//non-string variable
var string = "string";
var number = 32;
var boolean = true;
console.log(string + number + boolean);

//String Templates
var greeting = `Hello`;

//string interpolation
var place = `World`;
var greet = `Hello ${place}!`
console.log(greet);

`a\\b` // = a\b
String.raw`a\\b` // = a\\b


//Section 7.2: Reverse String
function reverseStr(str){
    return str.split('').reverse().join('');
}
reverseStr('String');


//Section 7.4: Access character at index in string

var string = "Hello, World!";
console.log( string.charAt(4) );

var string = "Hello, World!";
console.log( string[4] );

var string = "Hello, World!";
console.log( string.charCodeAt(4) );

//Section 7.5: Escaping quotes
var text = 'L\'albero means tree in Italian';
console.log( text );"L'albero means tree in Italian"


var text = "I feel \"high\"";
console.log(text);

var content = "<p class=\"special\">Hello World!</p>"; 
var hello = '<p class="special">I\'d like to say "Hi"</p>';
console.log(content);
console.log(hello);

var hi = "<p class='special'>I'd like to say &quot;Hi&quot;</p>"; 
var hello = '<p class="special">I&apos;d like to say "Hi"</p>';
console.log(hi);
console.log(hello);

