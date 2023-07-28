<script setup>
import { ref } from 'vue';

import tickets from './tickets.json';
// import users from './users.json';
import DashBoard_Table_Row from './DashBoard_Table_Row/DashBoard_Table_Row.vue';

const searchTerm = ref('');

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
                        <input type='text' placeholder="Search" v-model="searchTerm"/>
                    </td>
                    <td>
                        <button>Filter</button>
                    </td>
                </div>
            </tr>
            <tr>
                <td>
                    <h2>Id</h2>
                </td>
                <td>
                    <h2>Title</h2>
                </td>
                <td>
                    <h2>Assigned User</h2>
                </td>
                <td>
                    <h2>Status</h2>
                </td>
                <td>
                    <h2>Creation Date</h2>
                </td>
            </tr>
            <tr v-for="ticket in tickets" :key="ticket.id">
                <DashBoard_Table_Row v-if="ticket.id.includes(searchTerm) || ticket.title.includes(searchTerm) || ticket.assigned_user.username.includes(searchTerm) || ticket.created_date.includes(searchTerm)" :ticketData="ticket" />
            </tr>
            <!-- Create a mapping function to display tickets retrieved from the database -->
        </table>
        
    </div>
</template>

<style>
    @import './DashBoard.css';
</style>