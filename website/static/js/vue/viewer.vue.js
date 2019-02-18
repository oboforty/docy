export const template = `
  <div v-if="patient">

    <form action="" method="post" id="upload_form">
       <!--  TODO: FIXME: add csrf token via js  -->
       <!-- {% csrf_token %} -->

      <fieldset>
        <h2></h2>

        <div class="row">
          <div class="col">
            <label class="required" for="id_first_name">First name:</label>
            <input type="text" name="first_name" class="form-control" maxlength="20" required id="id_first_name">
          </div>
          <div class="col">
            <label class="required" for="id_last_name">Last name:</label>
            <input type="text" name="last_name" class="form-control" maxlength="20" required id="id_last_name"><br/>
          </div>
        </div>

        <label class="required" for="id_birth_date">Birth date:</label>
        <input type="date" name="birth_date" class="vDateField" size="10" required id="id_birth_date">

        <label class="required" for="id_gender">Gender:</label>
        <select name="gender" required id="id_gender">
            <option value="" selected>---------</option>
            <option value="1">Male</option>
            <option value="2">Female</option>
        </select>

        <label class="required" for="id_age">Age:</label>
        <input type="number" name="age" class="vIntegerField" required id="id_age">

        <label class="required" for="id_weight">Weight:</label>
        <input type="number" name="weight" step="any" required id="id_weight"><br/>

        <input type="checkbox" name="Chemo" id="id_Chemo"><label class="vCheckboxLabel" for="id_Chemo">Chemo</label><br/>
        <label class="required" for="id_Last_Chemo">Last Chemo:</label>
        <input type="date" name="Last_Chemo" class="vDateField" size="10" required id="id_Last_Chemo"><br/>

        <label class="required" for="id_Packs_yearly">Packs yearly:</label>
        <input type="number" name="Packs_yearly" class="vIntegerField" required id="id_Packs_yearly"><br/>


        <input type="checkbox" name="diabetes" id="id_diabetes"><label class="vCheckboxLabel" for="id_diabetes">Diabetes</label>

        <input type="checkbox" name="insulin" id="id_insulin"><label class="vCheckboxLabel" for="id_insulin">Insulin</label>

        <input type="checkbox" name="smoker" id="id_smoker"><label class="vCheckboxLabel" for="id_smoker">Smoker</label>

      </fieldset><br/>
    </form>


  </div>
`;