<script setup>
    import { ref, reactive, onMounted, computed } from 'vue';
    import tickets from './tickets.json';
    import CreateEditTicket from '../Tickets/CreateEditTicket.vue';
    import SingleTicket from '../Tickets/SingleTicket.vue';
    import DashBoard_Table_Row from './DashBoard_Table_Row/DashBoard_Table_Row.vue';
    import CreateEditUser from '../Users/CreateEditUser.vue';
    import UserProfile from '../Users/UserProfile.vue';
    import axios from 'axios';
    import LoginForm from '../LoginForm/LoginForm.vue';


    const modalData = ref();
    const searchTerm = ref('');
    const searchTermCheck = ref('');
    const singleTicketVisable = ref(false);
    const createVisable = ref(false);
    const editVisable = ref(false);
    const userFormVisable = ref(false);
    const userProfileVisable = ref(false);
    const loginFormVisable = ref(false);
    const user = ref('Guest');
    const tableData = ref(tickets);
    const filteredTableData = ref(tickets);
    const rowsPerPage = 5;
    const currentPage = ref(1);
    const maxPaginationButtons = 5;
    const currentPageDisplayData = ref();
    const paginationRange = ref({
        maxLeft : 1,
        maxRight : 5
    })
    const filterTerm = ref('Filter');

    const dummyData = {
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
                
    const getTickets = async () => {
        try {
            let response = await axios.get(
                `http://127.0.0.1:8000/user/`
            );
            console.log(response.data);
            // modalData == response.data;
            // console.log(modalData);
        } catch (error) {
            console.log(error.response.data);
        }
    }

    function totalRows() {
        if(searchTerm.value != '') {
            return filteredTableData.value.length;
        } else {
            return tableData.value.length;
        }
    };
            
    function totalPages() {
        return Math.ceil(totalRows() / rowsPerPage);
    };
    
    const currentPageDataInfo = computed(() => {
        if (searchTerm.value != searchTermCheck.value) {
            filterTableData();
        }
        paginationButton();
        const startIndex = (currentPage.value - 1) * rowsPerPage;
        const endIndex = startIndex + rowsPerPage;
        return filteredTableData.value.slice(startIndex, endIndex);
    })

    function filterTableData() {
        let tempFilteredTableData = [];
        currentPage.value = 1;
        console.log(filterTerm.value)
        switch (filterTerm.value) {
            case 'Filter':
                break;
            case 'Id':
                for(let i = 0; i < tableData.value.length; i++) {
                    // can this all be condensed to switch case or create additional if statements?
                    if (
                        tableData.value[i].id.includes(searchTerm.value)
                    ) {
                        tempFilteredTableData.push(tableData.value[i]);
        
                    }
                }
                
                searchTermCheck.value = searchTerm.value
                filteredTableData.value = tempFilteredTableData; 
            case 'Title':
                for(let i = 0; i < tableData.value.length; i++) {
                    // can this all be condensed to switch case or create additional if statements?
                    if (
                        tableData.value[i].title.includes(searchTerm.value)
                    ) {
                        tempFilteredTableData.push(tableData.value[i]);
                    }
                }

                searchTermCheck.value = searchTerm.value
                filteredTableData.value = tempFilteredTableData;   

            case 'Assigned User':
                for(let i = 0; i < tableData.value.length; i++) {
                    // can this all be condensed to switch case or create additional if statements?
                    if (
                        tableData.value[i].assigned_user.username.includes(searchTerm.value)
                    ) {
                        tempFilteredTableData.push(tableData.value[i]);
                    }
                }

                searchTermCheck.value = searchTerm.value
                filteredTableData.value = tempFilteredTableData;  

            case 'Status':
                for(let i = 0; i < tableData.value.length; i++) {
                    // can this all be condensed to switch case or create additional if statements?
                    if (
                        tableData.value[i].status_id == (searchTerm.value)
                    ) {
                        tempFilteredTableData.push(tableData.value[i]);
                    }
                }

                searchTermCheck.value = searchTerm.value
                filteredTableData.value = tempFilteredTableData;  

            case 'Creation Date':
                for(let i = 0; i < tableData.value.length; i++) {
                    // can this all be condensed to switch case or create additional if statements?
                    if (
                        tableData.value[i].created_date.includes(searchTerm.value)
                    ) {
                        tempFilteredTableData.push(tableData.value[i]);
                    }
                }

                searchTermCheck.value = searchTerm.value
                filteredTableData.value = tempFilteredTableData; 
                    
        }

    }
    

    function showModal(modalType, ticketData) {
        switch(modalType) {
            case 'createTicket':
                createVisable.value = true;
                singleTicketVisable.value = false;
                editVisable.value = false;
                break;
            case 'singleTicket':
                modalData.value = ticketData;
                singleTicketVisable.value = true;
                createVisable.value = false;
                editVisable.value = false;
                break;
            case 'editTicket':
                modalData.value = ticketData;
                editVisable.value = true;
                createVisable.value = false;
                singleTicketVisable.value = false;
                break;
            case 'userForm':
                userFormVisable.value = true;
                userProfileVisable.value = false;
                break;
            case 'userProfile':
                userProfileVisable.value = true;
                userFormVisable.value = false;
                break;
            case 'loginForm':
                loginFormVisable.value = true;
                break;
        }
                    
    }
            // CLOSE MODAL WITH ARGUEMENT
    function closeModal(modalType) {
        switch(modalType) {
            case 'createTicket':
                createVisable.value = false;
                break;
            case 'singleTicket':
                singleTicketVisable.value = false;
                break;
            case 'editTicket':
                editVisable.value = false;
                break;
            case 'userForm':
                userFormVisable.value = false;
            case 'userProfile':
                userProfileVisable.value = false;
                break;
        }
    }

    function paginationButton() {
        let maxLeft = (currentPage.value - Math.floor(maxPaginationButtons /2));
        let maxRight = (currentPage.value + Math.floor(maxPaginationButtons /2));
        if (maxLeft < 1) {
            maxLeft = 1;
            maxRight = maxPaginationButtons
        }
        if (maxRight > totalPages()) {
            maxLeft = totalPages() - (maxPaginationButtons - 1);
            maxRight = totalPages()
            if (maxLeft < 1) {
                maxLeft = 1;
            }
        }
        paginationRange.value = {
            maxLeft: maxLeft,
            maxRight: maxRight
        }
    }

    function range(start, end) {
        return Array.from({ length: end - start + 1 }, (_, index) => start + index);
    }

    function prevPage() {
        if(currentPage.value > 1) {
            currentPage.value--;
        }
    }

    function nextPage() {
        if (currentPage.value < totalPages()) {
            currentPage.value++;
        }
    }
            
    function gotoPage(pageNumber) {
        currentPage.value = pageNumber;
    }

    // CLOSE MODAL
    function close() {
    // uses Options API to emit a custom event
        this.$emit('close');
    }

    function changeVariables(filterTermChange) {
        filterTerm.value = filterTermChange;
        searchTerm.value = ''
    }

    function receiveEmit(user){
        alert('Loged in user is:' + user);
    }
</script>

<template>
    <LoginForm
        v-if="loginFormVisable"
        @close="closeModal('loginForm')"
        @user="receiveEmit"
    />
    <div id="container">
        <div id="nav">
            <!-- Test Button -->
            <button @click="getTickets()">Test</button>
            <h2>Welcome, User</h2>
            
            <div v-if="user">
                <h2>Welcome, {{user}}</h2>
            </div>
            <!-- <div v-if="user">
                <h2>Welcome, {{ this.$parent.$ref.user.username }}</h2>
            </div>-->
            
            <div>
                <img src="../../assets/userProfile.svg"/> 
                <a>Logout</a>
            </div>
            <button @click="showModal('loginForm')" class="btn btn-success">Login</button>
            <button @click="showModal('createTicket')" class="btn btn-primary">Create Ticket</button>
            <button @click="showModal('userForm')" class="btn btn-outline-secondary">Create User</button>
            <button @click="showModal('userProfile')"
            class="btn btn-outline-success"
            >Profile</button>
        </div>
        <div class="dashboard">
            <div class="dashboard-header">
                <input type='text' placeholder="Search" v-model="searchTerm"/>
                <div class="dropdown">
                    <button id="filter-button" class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="true">
                        {{filterTerm}}
                    </button>
                    <ul class="dropdown-menu">
                        <li @click="changeVariables('Id')">Id</li>
                        <li @click="changeVariables('Title')">Title</li>
                        <li @click="changeVariables('Assigned User')">Assigned User</li>
                        <li @click="changeVariables('Status')">Status</li>
                        <li @click="changeVariables('Creation Date')">Creation Date</li>
                        <li @click="changeVariables('Filter')">Remove Filter</li>
                    </ul>
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
                        <tr v-for="(row, index) in currentPageDataInfo" :key="index" class="ticket-data" 
                            @click="showModal('singleTicket', row)">
                            <DashBoard_Table_Row :ticketData="row"/>
                        </tr>
                    </tbody>
                </table>
            </div>
            <nav class="pagination-container">
                <div class="pagination">
                    <button @click="prevPage()" class="pagination-button" :class="{ disabled: currentPage === 1 }">Previous</button>
                    <button v-for="pageNumber in range(paginationRange.maxLeft, paginationRange.maxRight)"
                        :key="pageNumber"
                        @click="gotoPage(pageNumber)" 
                        :class="{ active: currentPage === pageNumber }"
                        class="pagination-button" >
                    {{ pageNumber }}
                    </button>
                    <button @click="nextPage()" class="pagination-button" :class="{ disabled: currentPage === totalPages }">Next</button>
                </div>
            </nav>
        </div>
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
        <SingleTicket v-if="singleTicketVisable" @close="closeModal('singleTicket')" :ticketData="modalData" :openEditTicket="showModal"/>
        <!--Opens User Create Modal-->
        <CreateEditUser
            v-if="userFormVisable" 
            @close="closeModal('userForm')"
            :openUserProfile="showModal"
        />
        <!--Opens user profile-->
        <UserProfile
            v-if="userProfileVisable"
            @close="closeModal('userProfile')"
            :openEditUser="showModal"
        />
        
    </template>

<style>
    @import './DashBoard.css';
</style>