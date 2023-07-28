<script setup>
import { ref } from 'vue';

import tickets from './tickets.json';
// import users from './users.json';
import DashBoard_Table_Row from './DashBoard_Table_Row/DashBoard_Table_Row.vue';

const searchTerm = ref('');

</script>

<template>
    <div>
        <div class="dashboard-header">
            <div>
                <button>All</button>
                <button>Mine</button>
            </div>
            <div>
                <input type='text' placeholder="Search" v-model="searchTerm"/>
                <button>Filter</button>
            </div>
        </div>
        <table class="dashboard-table">
            <thead>
                <tr>
                    <th>
                        <h2>Id</h2>
                    </th>
                    <th>
                        <h2>Title</h2>
                    </th>
                    <th>
                        <h2>Assigned User</h2>
                    </th>
                    <th>
                        <h2>Status</h2>
                    </th>
                    <th>
                        <h2>Creation Date</h2>
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="ticket in tickets" :key="ticket.id">
                    <DashBoard_Table_Row v-if="ticket.id.includes(searchTerm) || ticket.title.includes(searchTerm) || ticket.assigned_user.username.includes(searchTerm) || ticket.created_date.includes(searchTerm)" :ticketData="ticket" />
                </tr>
            </tbody>

            <!-- Create a mapping function to display tickets retrieved from the database -->
        </table>
        
    </div>
</template>

<style>
    @import './DashBoard.css';
</style>