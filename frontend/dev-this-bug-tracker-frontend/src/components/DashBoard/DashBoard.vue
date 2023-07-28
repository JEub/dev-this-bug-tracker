<script setup>

import tickets from './tickets.json';
import users from './users.json';

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
            <!-- Create a mapping function to display tickets retrieved from the database -->
        </table>
        
    </div>
</template>

<style>
    @import './DashBoard.css';
</style>