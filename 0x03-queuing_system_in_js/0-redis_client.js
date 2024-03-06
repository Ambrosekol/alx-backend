#!/usr/bin/node
/**
 * A script that logs into a reddis server
 */

import { createClient } from 'redis';

const server = createClient();

server.on('error', (err) => {
    console.log("Redis client not connected to the server: ", err.tostring());
});

server.on('connect', () => {
    console.log("Redis client connected to the server");
});
