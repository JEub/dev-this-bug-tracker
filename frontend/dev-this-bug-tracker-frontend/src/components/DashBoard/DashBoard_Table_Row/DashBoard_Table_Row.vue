<script>
export default {
    props: {
        ticketData: Object
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


