<script setup>

import tickets from './tickets.json';
import users from './users.json';
import DashBoard_Table_Row from './DashBoard_Table_Row/DashBoard_Table_Row.vue';

console.log(tickets);
console.log(users);





</script>

<template>
    <div>
        <table class="dashboard-table">
            <tr class="dashboard-header">
                <div>
                    <td>
                        <button>All</button>
                    </td>
                    <td>
                        <button>Mine</button>
                    </td>
                </div>
                <div>
                    <td>
                        <input placeholder="Search"/>
                    </td>
                    <td>
                        <button>Filter</button>
                    </td>
                </div>
            </tr>
            <div v-for="ticket in tickets" :key="ticket.id">
                <DashBoard_Table_Row :ticketData="ticket" />
            </div>
            <!-- Create a mapping function to display tickets retrieved from the database -->
        </table>
        
    </div>
</template>

<!-- <script>
    export default {
        props: [tickets, users]
    }
</script> -->

<style>
    @import './DashBoard.css';
</style>