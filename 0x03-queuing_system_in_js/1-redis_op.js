#!/usr/bin/node
/**
 * A script that logs into a reddis server
 */

import { createClient, print } from 'redis';

const server = createClient();

server.on('error', (err) => {
    console.log("Redis client not connected to the server: ", err.tostring());
});

server.on('connect', () => {
    console.log("Redis client connected to the server");
});

function setNewSchool(schoolName, value) {
    server.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
    server.get(schoolName, (err, reply) => {
        if (err) {
            console.error(err);
            throw err;
        }
        console.log(reply);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
