<script setup>
    import { ref } from 'vue';
    
    const title = ref('Title')
    const description = ref('Description')
    const storyPoints = ref('Story Points')
    const ticketStatus = ref('Open')
    const groups = ref(['Retail'])
    const assignedUser = ref(['Jack'])
    const parentLinks = ref('Parent Links')
    const ticketTags = ref('Ticket Tags')
    const ticketComments = ref('Ticket Comments')
    // add user to ticket
    // add comment button for view
</script>

<template>
    <!-- pull data from database -->
    <div class="body">
        <div class="header">
                <h3>Ticket id</h3>
                <h3>Creator contact email</h3>
                <h3>Assigned users</h3>
                <h3>Ticket status</h3>
        </div>
        <div class="body">
            <div class="row">
                <p>Date opened / closed</p>
            </div>
            <div class="header">
                <p>Title</p>
                <p>Description</p>
            </div>
            <div class="row">Groups</div>
            <div class="row">Story points</div>
            <div class="row">
                <ul>
                    <li>Parent ticket links</li>
                </ul>
            </div>
            <div class="row">
                <ul>
                    <li>History of assigned users w/time worked on ticket</li>
                </ul>
            </div>
            <div class="row">
                <p>Ticket tags</p>
            </div>
            <div class="body">
                <div class="row bigRow">
                    <button class="button"><a href="">Add Comment</a></button>
                    <div class="hide">
                        <p>Ticket comments 1</p>
                        <p>Ticket comments 2</p>
                        <p>Ticket comments 3</p>
                        <p>Ticket comments 4</p>
                        <p>Ticket comments 5</p>
                        <p>Ticket comments 6</p>
                        <p>Ticket comments 7</p>
                        <p>Ticket comments 8</p>
                        <p>Ticket comments 9</p>
                        <p>Ticket comments 10</p>
                        <p>Ticket comments 11</p>
                        <p>Ticket comments 12</p>
                        <p>Ticket comments 13</p>
                        <p>Ticket comments 14</p>
                        <p>Ticket comments 15</p>
                        <p>Ticket comments 16</p>
                    </div>
                </div>
            </div>
            <div class="header">
            <!-- both of these buttons could open new modal? -->
                
                <button class="button"><a href="">Edit Ticket</a></button>
            </div>
        </div>
    </div>
    
</template>

<style>
@import './SingleTicket.css';
</style>