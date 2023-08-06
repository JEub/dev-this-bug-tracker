<script>
export default {
    props: {
        ticketData: {
      "id": String,
      "title": String,
      "description": String,
      "start_date": Date,
      "completed_date": Date,
      "status_id": Number,
      "creator": {
        "id": String,
        "username": String,
        "email": String
      },
      "assigned_user": {
        "id": Number,
        "username": String,
        "email": String
      }, 
      "created_date": Date,
      "last_update": Date,
    }
    }
}
</script>


<template>
    <td>{{ ticketData.id }}</td>
    <td>{{ ticketData.title }}</td>
    <td>{{ ticketData.assigned_user.username }}</td>
    <td>{{ ticketData.status_id }}</td>
    <td>{{ ticketData.created_date }}</td>
</template>

<!-- <style>
    @import './DashBoard_Table_Row.css';
</style> -->