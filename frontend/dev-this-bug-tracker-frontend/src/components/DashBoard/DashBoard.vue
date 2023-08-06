<script setup>
import { ref } from 'vue';

import tickets from './tickets.json';
import CreateEditTicket from '../Tickets/CreateEditTicket.vue'
// import users from './users.json';
import DashBoard_Table_Row from './DashBoard_Table_Row/DashBoard_Table_Row.vue';




</script>


<script>
    const searchTerm = ref('');

    export default {
    name: 'DashBoard',
    components: {
      CreateEditTicket,
    },
    data() {
      return {
        tableData: tickets,
        rowsPerPage: 5,
        currentPage: 1,
        modalData: null,
        isModalVisible: false,
      };
    },
    computed: {
        totalRows() {
            return this.tableData.length;
        },
        totalPages() {
            return Math.ceil(this.totalRows / this.rowsPerPage);
        },
        currentPageData() {
            const startIndex = (this.currentPage - 1) * this.rowsPerPage;
            const endIndex = startIndex + this.rowsPerPage;
            return this.tableData.slice(startIndex, endIndex);
        },
    },
    methods: {
      showModal(ticketData) {
        console.log('test?')
        this.modalData = ticketData;
        this.isModalVisible = true;
      },
      closeModal() {
        this.isModalVisible = false;
      },
      prevPage() {
        if(this.currentPage > 1) {
            this.currentPage--;
        }
      },
      nextPage() {
        if (this.currentPage < this.totalPages) {
            this.currentPage++;
        }
      },
      gottoPage(pageNumber) {
        this.currentPage = pageNumber;
      }
    }
  };
</script>

<template>
    <div class="dashboard">
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

        <table id="myTable" class="dashboard-table">
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
                <tr v-for="(row, index) in currentPageData" :key="index" class="ticket-data" @click="showModal(ticket)">
                    <DashBoard_Table_Row 
                    v-if="row.id.includes(searchTerm) || ticket.title.includes(searchTerm) || ticket.assigned_user.username.includes(searchTerm) || ticket.created_date.includes(searchTerm)" :ticketData="row" 
                    />
                </tr>
            </tbody>
            
        </table>
        <nav>
            <ul class="pagination">
                <li @click="prevPage" :class="{ disabled: currentPage === 1 }">Previous</li>
                <li v-for="pageNumber in totalPages"
                    :key="pageNumber"
                    @click="gotoPage(pageNumber)"
                    :class="{ active: currentPage === pageNumber }"
                >
                {{ pageNumber }}
                </li>
                <li @click="nextPage" :class="{ disabled: currentPage === totalPages }">Next</li>
            </ul>
        </nav>
    </div>
        <CreateEditTicket
        v-show="isModalVisible"
        @close="closeModal"
        class="modal-popup"
        :ticket="modalData"
    />
</template>

<style>
    @import './DashBoard.css';
    /* @import 'https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/css/bootstrap.min.css';
    @import 'https://cdn.datatables.net/1.13.6/css/dataTables.bootstrap5.min.css'; */
</style>