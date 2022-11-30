#!/usr/bin/node
//class declaration and more

class Person {

	name;

	constructor(name) {
		this.name = name;
	}

	introduceSelf() {
		console.log(`Hi! I'm ${this.name}`);
	}
}

class Professor extends Person {

	teaches;

	constructor(name, teaches) {
		super(name);
		this.teaches = teaches;
	}

	introduceSelf() {
		console.log(`My name is ${this.name}, and I will be your ${this.teaches} professor.`);
	}

	grade(paper) {
		const grade = Math.floor(Math.random() * (5 - 1) + 1);
		console.log(grade);
	}
}

class Student extends Person {

	#year;

	constructor(name, year) {
		super(name);
		this.#year = year;
	}

	introduceSelf() {
		console.log(`Hi! I'm ${this.name}, and I'm in year ${this.#year}.`);
	}

	canStudyArchery() {
		this.#year > 1;
	}
}

class ChatBot {
	#room = 0;

	constructor(room) {
		this.#room = room;
	}

	startChat() {
		this.#welcomeMessage();
		}

	#welcomeMessage() {
		console.log(`Welcome to room ${this.#room}.`);
	}
}

//try code 1
const giles = new Person('Giles');
giles.introduceSelf();

//try code 2
const walsh = new Professor('Walsh', 'Psychology');
walsh.introduceSelf();  // 'My name is Walsh, and I will be your Psychology professor'
walsh.grade('my paper'); // some random grade

//try code 3
const summers = new Student('Summers', 2);
summers.introduceSelf(); // Hi! I'm Summers, and I'm in year 2.
summers.canStudyArchery(); // true
//summers.#year; // SyntaxError

//try code 4
const newChat = new ChatBot(1);
newChat.startChat();
