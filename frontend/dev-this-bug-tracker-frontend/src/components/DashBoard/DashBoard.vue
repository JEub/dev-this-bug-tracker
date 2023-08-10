<script setup>
import { ref } from 'vue';
import tickets from './tickets.json';
import CreateEditTicket from '../Tickets/CreateEditTicket.vue';
import TicketModal from '../Tickets/TicketModal.vue';
import SingleTicket from '../Tickets/SingleTicket.vue';
// import users from './users.json';
import DashBoard_Table_Row from './DashBoard_Table_Row/DashBoard_Table_Row.vue';

// const searchTerm = ref('');
// const isOpen = ref(false)
// const singleTicketOpen = ref(false)
// const isModalVisible= ref(false)
// const toggleModal = () => {
//     alert( 'You toggled open modal' );
//     isOpen.value = !isOpen.value;
//     return toggleModal;
// };
// const createToggle = () => {
//     alert( 'You toggled create modal' );
//     // createOpen.value = !createOpen.value;
//     isModalVisible.value = !isModalVisible.value;
//     return createToggle;
// };
// const singleToggle = () => {
//     alert( 'You toggled single modal' );
//     singleTicketOpen.value = !singleTicketOpen.value;
// };
</script>


<script>
    const searchTerm = ref('');
    
    // const filteredTableData = ref([])
    export default {
        name: 'DashBoard',
        components: {
            CreateEditTicket,
            DashBoard_Table_Row,
            SingleTicket,
            TicketModal
        },
        data () {
            return {
                modalData: null,
                singleTicketVisable: false,
                createVisable: false,
                editVisable: false,
                tableData: tickets,
                filteredTableData: tickets,
                rowsPerPage: 5,
                currentPage: 1,
                maxPaginationButtons: 5,
                paginationRange: {
                    maxLeft: 1,
                    maxRight: 5,
                },
                dummyData:{
                    id: null,
                    title: null,
                    description: null,
                    start_date: null,
                    completed_date: null,
                    status_id: null,
                    creator: {
                        id: null,
                        username: null,
                        email: null,
                    },
                    assigned_user: {
                        id: null,
                        username: null,
                        email: null,
                    }, 
                    created_date: null,
                    last_update: null
                }
            };
        },
        computed: {
            totalRows() {
                if(searchTerm.value != '') {
                    return this.filteredTableData.length;
                } else {
                    return this.tableData.length;
                }
            },
            totalPages() {
                return Math.ceil(this.totalRows / this.rowsPerPage);
            },

            currentPageData() {
                this.paginationButton();
                if (searchTerm.value != ''){
                    this.filterTableData
                    const startIndex = (this.currentPage - 1) * this.rowsPerPage;
                    const endIndex = startIndex + this.rowsPerPage;
                    return this.filteredTableData.slice(startIndex, endIndex);
                } else {
                    const startIndex = (this.currentPage - 1) * this.rowsPerPage;
                    const endIndex = startIndex + this.rowsPerPage;
                    return this.tableData.slice(startIndex, endIndex);
                }
            },
            filterTableData() {
                console.log('filtering')
                let filteredTableData = [];
                this.currentPage = 1;
                    for(let i = 0; i < this.tableData.length; i++) {
                        if (this.tableData[i].id.includes(searchTerm.value) || this.tableData[i].title.includes(searchTerm.value) || this.tableData[i].assigned_user.username.includes(searchTerm.value) || this.tableData[i].created_date.includes(searchTerm.value)) {
                            filteredTableData.push(this.tableData[i]);
                        }
                    }
                    this.filteredTableData = filteredTableData;
            }
        },
        methods: {
            showModal(modalType, ticketData) {
                switch(modalType) {
                    case 'createTicket':
                        console.log('Opening Create ticket modal!');
                        this.createVisable = true;
                        this.singleTicketVisable = false;
                        this.editVisable = false;
                        break;
                    case 'singleTicket':
                        console.log("Opening single ticket modal!");
                        this.modalData = ticketData;
                        this.singleTicketVisable = true;
                        this.createVisable = false;
                        this.editVisable = false;
                        break;
                    case 'editTicket':
                        console.log('Opening Edit ticket modal!');
                        this.modalData = ticketData;
                        this.editVisable = true;
                        this.createVisable = false;
                        this.singleTicketVisable = false;
                        break;
                    }
            },
            closeModal(modalType) {
                switch(modalType) {
                    case 'createTicket':
                        console.log('Closing Create ticket modal!');
                        this.createVisable = false;
                        break;
                    case 'singleTicket':
                        console.log("Closing single ticket modal!");
                        this.singleTicketVisable = false;
                        break;
                    case 'editTicket':
                        console.log('Closing Edit ticket modal!');
                        this.editVisable = false;
                        break;
                    }
            },
            paginationButton() {
                let maxLeft = (this.currentPage - Math.floor(this.maxPaginationButtons /2));
                let maxRight = (this.currentPage + Math.floor(this.maxPaginationButtons /2));
                console.log('176', maxLeft, maxRight)
                if (maxLeft < 1) {
                    maxLeft = 1;
                    maxRight = this.maxPaginationButtons
                }

                if (maxRight > this.totalPages) {
                    maxLeft = this.totalPages - (this.maxPaginationButtons - 1);
                    maxRight = this.totalPages

                    console.log('186', maxLeft, maxRight)
                    if (maxLeft < 1) {
                        maxLeft = 1;
                    }
                }
                this.paginationRange = {
                    'maxLeft': maxLeft,
                    'maxRight': maxRight
                }
            },
            range(start, end) {
                return Array.from({ length: end - start + 1 }, (_, index) => start + index);
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
            gotoPage(pageNumber) {
                this.currentPage = pageNumber;
            },
            close() {
            // uses Options API to emit a custom event
                this.$emit('close');
            },
        },
    };
</script>

<template>
    <div  >
        <button @click="showModal('createTicket')" class="btn btn-primary">Create Ticket</button>
    </div>
    <div class="dashboard">
        <div class="dashboard-header">
            <div>
                <button class="btn btn-outline-primary">All</button>
                <button class="btn btn-primary">Mine</button>
            </div>
            <div>
                <input type='text' placeholder="Search" v-model="searchTerm"/>
                <button>Filter</button>
            </div>
        </div> 
        <div class="table-data-container">
            <table id="myTable" class="table table-striped table-hover dashboard-table">
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
                    <tr v-for="(row, index) in currentPageData" :key="index" class="ticket-data" 
                        @click="showModal('singleTicket', row)">
                        <DashBoard_Table_Row :ticketData="row"/>
                    </tr>
                </tbody>
                
            </table>
        </div>

        
        <nav class="pagination-container">
            <div class="pagination">
                <button @click="prevPage" class="pagination-button" :class="{ disabled: currentPage === 1 }">Previous</button>
                <button v-for="pageNumber in range(this.paginationRange.maxLeft, this.paginationRange.maxRight)"
                    :key="pageNumber"
                    @click="gotoPage(pageNumber)"
                    :class="{ active: currentPage === pageNumber }"
                    class="pagination-button" >
                {{ pageNumber }}
                </button>
                <button @click="nextPage" class="pagination-button" :class="{ disabled: currentPage === totalPages }">Next</button>
            </div>
        </nav>
    </div>
        <!-- Opens Edit Ticket Component -->
        <CreateEditTicket
            v-if="editVisable"
            @close="closeModal('editTicket')"
            class="modal-popup"
            :ticketData="modalData"
        /> 
        <!-- Opens Create Ticket Component -->
        <CreateEditTicket
            v-if="createVisable"
            @close="closeModal('createTicket')"
            class="modal-popup"
            :ticketData="dummyData"
        /> 
        <!--edit ticket to close modal and open edit modal-->
        <SingleTicket v-if="singleTicketVisable" @close="closeModal('singleTicket')" :ticketData="modalData" :openEditTicket="showModal"/>
        <!--<CreateEditTicket
            v-show="singleTicketVisable"
            @click="toggleModal"
        />-->
    </template>

<style>
    @import './DashBoard.css';
</style>