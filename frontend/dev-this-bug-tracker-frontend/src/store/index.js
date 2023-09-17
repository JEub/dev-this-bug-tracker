// Here we’ll be calling the auth method that handled everything and storing it in Vuex’s store component.
import {createApp} from 'vue';
import { createStore } from 'vuex'

const store =  createStore({
    state() {
        return{
            email: "",
        }
    },
    mutations: {
        login(state, email) {
            state.email = email;
            localStorage.setItem('email', email);
            alert("Logged In");
        },
        logout(state) {
            state.email = "";
            localStorage.removeItem('email');
            alert("Logged Out");
        },
        initialiseStore(state) {
            if(localStorage.getItem('email')){
                state.email = localStorage.getItem('email')
            }
        }
    }
})
const app = createApp({Homeview})
app.use(store)