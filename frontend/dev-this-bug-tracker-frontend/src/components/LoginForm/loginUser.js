import {reactive} from 'vue'


export const loggedUser = reactive({
    email: 'someone@email.com',
    username: 'Guest R',
    loggedIn: false,
    login(username){
        loggedIn = true;
        this.username = username.value;
    }
    });